from sqlalchemy import Column,Integer,String
from config.database import Base

class Student(Base):
    __tablename__ = "student"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable = False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    student_class = Column(String(100),nullable = False)