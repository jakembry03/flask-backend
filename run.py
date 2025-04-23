from app.routes import app
from app.database import setup_database

if __name__ == '__main__':
    setup_database()  # Initialize the database
    app.run(debug=True)