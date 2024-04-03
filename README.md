# Mock Task Management API

1. fork the project directiory
2. activate venv and install dependencies
   -  windows: \venv\Scripts\activate
   -  linux: source venv/bin/activate
   -  pip3 install -r requirements.txt
3. execute python app.py or python3 app.py

## Get a list of all tasks on http://localhost:8000/tasks
## Post a new task to http://localhost:8000/tasks
## Update a task using at http://localhost:8000/tasks/int:task_id
## Delete a task at http://localhost:8000/tasks/int:task_id

## Task structure
 { id: int, position: int, category: string, title: string, status: string, description: string }

 ## You only need to send a title, category and description when creating a new task.
