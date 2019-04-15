# Python-Todo-List-CLI

## Demo of the app
---


TABLE NAME: TO DO LIST (MAIN TABLE) ORDER BY ID    
```
+-------------------------------------------------------------------------------------------------------------+
|  id   |                tasks                |           create_at            |   completion    | project_id |
+ =========================================================================================================== +
|   1   | fry eggs                            |      Mon, 15 April, 19:17      |   Unfinished    |     1      |
+-------------------------------------------------------------------------------------------------------------+
|   2   | fry eggs                            |      Mon, 15 April, 19:17      |    Finished     |     2      |
+-------------------------------------------------------------------------------------------------------------+
|   4   | d4s                                 |      Mon, 15 April, 19:17      |   Unfinished    |     4      |
+-------------------------------------------------------------------------------------------------------------+
|   5   | d5                                  |      Mon, 15 April, 19:37      |   Unfinished    |     2      |
+-------------------------------------------------------------------------------------------------------------+
```

                              TO DO LIST DETAILS   
```                              
+--------------------------------------------------------------------------------------+
|   project_id    |             description             |      completion      |  id   |
+ ==================================================================================== +
|        1        | d1                                  |      Unfinished      |   1   |
+--------------------------------------------------------------------------------------+
|        2        | d5                                  |      Unfinished      |   5   |
+--------------------------------------------------------------------------------------+
|        4        | d4                                  |      Unfinished      |   4   |
+--------------------------------------------------------------------------------------+
```

### Requirements
---
[x] The user can run your program from the command line.
[x] If the user does not supply the correct arguments, or supplies a --help flag, the user sees a "usage" message. 
[x] The user can add a todo from the command line, by calling add_todo. The fields specified should be text, due_date, and project_id. The fields due_date and project_id are optional. Text is required.
[x] Todos added, by default should be marked as incomplete.
[x] The user should see a message giving information about the todo that was added.
[x] The user can call a function called mark_complete and pass the id of the todo to mark complete. 
[x] The user can see all todos from the command line by passing a list command, sorted with the ones due first. 
[ ] The user can supply arguments to the list command to only see todos that are complete. 
[x] The user can supply arguments to the list command to only see todos of a particular project_id. 
[x] The user can supply arguments to the list command to reverse the default sort, to now see the todos by due_date descending.
[x] The user can supply arguments to the list command to combine the above options.

Optional Requirements
[ ] The user can add a project by calling add_project. Each project must have a name. 
[ ] The user can see all projects from the command line.

Bonus Requirements
[ ] The user can add a user_id to each todo. 
[ ] The user can add a user to the system by passing add_user. Each user should have a name, email_address, and id. 
[ ] The user can call a list_users command that shows all the users in the system.
[ ] The user can call a staff command that shows each project, combined with each of the users working on that project.
[ ] The user can call a who_to_fire command that lists all users who are not currently assigned a todo.
