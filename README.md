## Kanban Board

### What is this app?
This is a Kanban Board application. It allows anyone to input the tasks they want to do, and give them statuses such as "done", "doing" or "to do". The users can easily update each task's status by moving one from one status to another. They can also delete a task once it's not relevant anymore.

### What does this folder have?
Basically, this folder includes a static sub-folder than contains a README.md file, a CSS file (styling for the user interface), a templates sub-folder than contains an HTML file, an app.py file that has the Flask code, a requirements.txt file that specifies the requirements to run this app and a todo.db database.

### What is the structure of the Python code?
First, I connect the app to a database where the data will be stored, and can be queried from.
Then, I create the table to store the data.
Next, I define different functions to query, add, update the statuses of, and delete tasks. They have to be made into routes so that whenever a user sends a request, the server knows which route to take and what to do from there, whether to update the task status or delete it.

### How to run

```python3.6 -m venv .venv 
source .venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=app.py
flask run
