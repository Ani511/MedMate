from sqlalchemy import Column, Integer, String
from database import Base  
class Medicine(Base):
    __tablename__ = "medicines"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    pharmacy = Column(String)
    location = Column(String)

class Reminder(Base):
    __tablename__ = "reminders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    medicine_name = Column(String)
    time = Column(String)

