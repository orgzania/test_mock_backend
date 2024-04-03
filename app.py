from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store (replace with a database for persistence)
tasks = {1: {"id": 1, "position": 1, "category": "Shopping", "title": "Grocery Shopping", "status": "pending", "description": "Go to Trader Joe's and get 6 eggs, 1 gal milk, 1 bread"},
         2: {"id": 2, "position": 2, "category": "Work", "title": "Feature Deadline - Slackbot", "status": "pending", "description": "Create a Slackbot to pull all Jira tasks and post in the team's channel"}}
next_id = 2  # Track the next available ID for tasks

# Function to generate a unique ID
def generate_id():
  global next_id
  next_id += 1
  return next_id

# GET: Retrieve all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
  return jsonify(list(tasks.values()))  # Convert tasks dict to list for JSON response

# POST: Create a new task
@app.route("/tasks", methods=["POST"])
def create_task():
  # Get data from request body
  data = request.get_json()
  if not data:
    return jsonify({"error": "Missing task data"}), 400

  # Generate ID and add task to dictionary
  task_id = generate_id()
  data["id"] = task_id
  data["position"] = task_id
  tasks[task_id] = data
  return jsonify({"message": "Task created", "task": data}), 201

# UPDATE: Update a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
  # Get data from request body
  data = request.get_json()
  if not data:
    return jsonify({"error": "Missing task data"}), 400

  # Check if task exists
  if task_id not in tasks:
    return jsonify({"error": "Task not found"}), 404

  # Update task in dictionary
  tasks[task_id] = data
  return jsonify({"message": "Task updated"})

# DELETE: Delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
  # Check if task exists
  if task_id not in tasks:
    return jsonify({"error": "Task not found"}), 404

  # Delete task from dictionary
  del tasks[task_id]
  return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
  app.run(debug=True, port=8000)
