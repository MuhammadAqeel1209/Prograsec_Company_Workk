from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False,unique=True)
    password = Column(String(200),nullable = False)
    student_class = Column(String(200), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)
    
    department = relationship("Department", back_populates="students") 
