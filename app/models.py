from sqlalchemy import Column, Integer, String, Date, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    deadline = Column(Date, nullable=False)
    importance = Column(Enum('low', 'high'), nullable=False)
    urgency = Column(Enum('low', 'high'), nullable=False)
    
    def get_color(self):
        """Determine the color based on importance and urgency."""
        if self.importance == 'low' and self.urgency == 'low':
            return 'blue'
        elif self.importance == 'high' and self.urgency == 'low':
            return 'green'
        elif self.importance == 'low' and self.urgency == 'high':
            return 'yellow'
        elif self.importance == 'high' and self.urgency == 'high':
            return 'red'