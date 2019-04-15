import sqlite3
import os
from datetime import date, datetime
import fire


DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con


def db_create_todo():
    con = db_connect()
    cur = con.cursor()

    todo_sql = """
        CREATE TABLE IF NOT EXISTS todo_list (
            id integer PRIMARY KEY,
            tasks text,
            create_at datetime,
            completion not null,
            project_id
        )
    """

    cur.execute(todo_sql)
    con.commit()
    con.close()
    db_create_detail()


def add_todo(id, task, details, project_id):
    con = db_connect()
    cur = con.cursor()

    today = date.today()
    now = datetime.now().strftime("%a, %d %B, %H:%M")

    add_sql = """
        INSERT INTO todo_list (id, tasks, create_at, completion, project_id)
        VALUES (?, ?, ?, ?, ?)
    """

    complete = "Unfinished"

    cur.execute(add_sql, (id, task, now, complete, project_id))
    con.commit()

    select_sql = """
        SELECT * from todo_list
    """

    cur.execute(select_sql)
    con.commit()
    con.close()

    if complete == 'Unfinished':
        add_todo_detail(project_id, details, complete, id)
    else:
        pass


def db_create_detail():
    con = db_connect()

    details_sql = """
    CREATE TABLE IF NOT EXISTS todo_details (
        project_id integer,
        description text,
        completion not null,
        id integer
    )
    """

    cur = con.cursor()
    cur.execute(details_sql)
    con.commit()
    con.close()
    create_detail_finished()


def create_detail_finished():
    con = db_connect()
    cur = con.cursor()

    details_finished = """
    CREATE TABLE IF NOT EXISTS finished_details (
        project_id integer,
        description text,
        finished_at null,
        id integer
    )
    """
    cur.execute(details_finished)
    con.commit()
    con.close()


def add_todo_detail(project_id, details, complete, id):
    con = db_connect()
    add_sql = """
        INSERT INTO todo_details (project_id, description, completion, id)
        VALUES (?, ?, ?, ?)
    """
    cur = con.cursor()
    cur.execute(add_sql, (project_id, details, complete, id))
    con.commit()

    select_sql = """
        SELECT * from todo_details
    """

    cur.execute(select_sql)
    con.commit()
    con.close()


def delete_table(table):
    con = db_connect()
    select_sql = """
    DELETE FROM {}
    """.format(table)
    cur = con.cursor()
    ask = input("Are you sure to delete this table (Y/N)?")
    if ask == 'Y' or ask == 'y':
        cur.execute(select_sql)
        con.commit()
        con.close()
        print('The table named {} has been deleted'.format(table))
    else:
        pass


def delete_row(table, id):
    con = db_connect()
    select_sql = """
    DELETE FROM {}
    WHERE project_id = {}
    """.format(table, id)
    cur = con.cursor()
    cur.execute(select_sql)
    con.commit()
    con.close()


def list_data(table, project_id=None, sort=None):
    con = db_connect()
    cur = con.cursor()

    dash = '+' + '-' * 109 + '+'
    line = '+ ' + '=' * 107 + ' +'

    if project_id == None and table == "todo_list" and sort == None:
        select_sql = """
        SELECT * from {}
        ORDER BY id
        """.format(table)
        cur.execute(select_sql)
        con.commit()
        data = cur.fetchall()
        print()
        print(' ' * 30,
              'TABLE NAME: TO DO LIST (MAIN TABLE) ORDER BY ID', ' ' * 30)
        print(dash)
        print('| {:^5s} | {:^35s} | {:^30s} | {:^15s} | {:<1s} |'.format(
            'id', 'tasks', 'create_at', 'completion', 'project_id'))
        print(line)

        for i in range(0, len(data)):
            print('| {:^5d} | {:<35s} | {:^30s} | {:^15s} | {:^10d} |'.format(
                data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))
            print(dash)
    elif project_id == None and table == "todo_list" and sort != None:
        select_sql = """
        SELECT * from {}
        ORDER BY create_at {}
        """.format(table, sort)
        cur.execute(select_sql)
        con.commit()
        data = cur.fetchall()
        print()
        print(' ' * 30,
              'TABLE NAME: TO DO LIST (MAIN TABLE) ORDER BY ID', ' ' * 30)
        print(dash)
        print('| {:^5s} | {:^35s} | {:^30s} | {:^15s} | {:<1s} |'.format(
            'id', 'tasks', 'create_at', 'completion', 'project_id'))
        print(line)

        for i in range(0, len(data)):
            print('| {:^5d} | {:<35s} | {:^30s} | {:^15s} | {:^10d} |'.format(
                data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))
            print(dash)

    elif project_id == None and table == "todo_details":
        select_sql = """
        SELECT * from {}
        Order by project_id
        """.format(table)
        cur.execute(select_sql)
        con.commit()
        data = cur.fetchall()
        dash = '+' + '-' * 86 + '+'
        line = '+ ' + '=' * 84 + ' +'
        print()
        print(' ' * 30, 'TO DO LIST DETAILS', ' ' * 30)
        print(dash)
        print('| {:^15s} | {:^35s} | {:^20s} | {:^5s} |'.format(
            'project_id', 'description', 'completion', 'id'))
        print(line)

        for i in range(0, len(data)):
            print('| {:^15d} | {:<35s} | {:^20s} | {:^5d} |'.format(
                data[i][0], data[i][1], data[i][2], data[i][3]))
            print(dash)
    elif project_id != None and table == "todo_details":
        select_sql = """
        SELECT * from {}
        WHERE project_id = {}
        """.format(table, project_id)
        cur.execute(select_sql)
        con.commit()
        data = cur.fetchall()
        dash = '+' + '-' * 86 + '+'
        line = '+ ' + '=' * 84 + ' +'
        print()
        print(' ' * 30, 'TO DO LIST DETAILS WITH project_id', ' ' * 30)
        print(dash)
        print('| {:^15s} | {:^35s} | {:^20s} | {:^5s} |'.format(
            'project_id', 'description', 'completion', 'id'))
        print(line)

        for i in range(0, len(data)):
            print('| {:^15d} | {:<35s} | {:^20s} | {:^5d} |'.format(
                data[i][0], data[i][1], data[i][2], data[i][3]))
            print(dash)
    else:
        print("Wrong Argument please try again")

    con.close()


def update_finished(table, id, finished_at):
    con = db_connect()
    sql = """
        INSERT INTO {}
        SELECT id, description, completion, project_id FROM todo_details
        WHERE id = {}
    """.format(table, id, finished_at)

    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

    con = db_connect()
    cur = con.cursor()
    mark = """
        UPDATE finished_details
        SET finished_at = ?
        WHERE id = ?;
    """
    cur = con.cursor()
    cur.execute(mark, (finished_at, id))
    con.commit()
    con.close()

    con = db_connect()
    cur = con.cursor()
    select_sql = """
        SELECT * from finished_details
    """
    cur.execute(select_sql)
    con.commit()
    con.close()


def mark_complete(id):
    now = datetime.now().strftime("%a, %d %B, %H:%M")
    con = db_connect()
    mark = """
        UPDATE todo_list
        SET completion = ?
        WHERE id = ?;
    """
    cur = con.cursor()
    cur.execute(mark, ('Finished', id))
    con.commit()
    con.close()
    delete_row("todo_details", id)
    update_finished("finished_details", id, now)


if __name__ == '__main__':
    fire.Fire()
