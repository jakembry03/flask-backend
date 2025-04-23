# Time-Saving App

This is a backend-focused time-saving app based on the Eisenhower Matrix, developed as part of a capstone project.

## Features
- Task Management System: Create, Read, Update, and Delete tasks.
- Eisenhower Matrix: Classify tasks into quadrants based on importance and urgency.
- Color Coding: Tasks are color-coded for prioritization (Blue, Green, Yellow, Red).
- Backend-Focused: Designed to study time-saving practices and their effectiveness.

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jakembry03/time-saving-app.git
   cd time-saving-app
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
1. Initialize the database:
   ```bash
   python -c "from app.database import setup_database; setup_database()"
   ```
2. Start the Flask server:
   ```bash
   python run.py
   ```
3. Access the API at `http://127.0.0.1:5000`.

## Project Structure
```
time-saving-app/
│
├── app/
│   ├── __init__.py        # Flask app initialization
│   ├── models.py          # Database models
│   ├── routes.py          # API endpoints
│   ├── services.py        # Eisenhower Matrix logic
│   └── database.py        # Database setup
│
├── run.py                 # Main entry point
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```
