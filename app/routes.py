from flask import Flask, request, jsonify
from app.models import Task
from app.database import Session

app = Flask(__name__)

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task."""
    data = request.json
    new_task = Task(
        title=data['title'],
        description=data.get('description'),
        deadline=data['deadline'],
        importance=data['importance'],
        urgency=data['urgency']
    )
    session = Session()
    session.add(new_task)
    session.commit()
    return jsonify({"message": "Task created successfully!"}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retrieve all tasks."""
    session = Session()
    tasks = session.query(Task).all()
    return jsonify([{
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "deadline": task.deadline,
        "importance": task.importance,
        "urgency": task.urgency,
        "color": task.get_color()
    } for task in tasks])

@app.route('/')
def home():
	return "Welcome to the Time-Saving App API!"