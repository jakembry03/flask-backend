from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

DATABASE_URI = 'sqlite:///eisenhower_matrix.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def setup_database():
    """Set up the database."""
    Base.metadata.create_all(engine)