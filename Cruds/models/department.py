from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base

class Department(Base):
    __tablename__ = 'departments'
    
    id = Column(Integer, primary_key=True,index= True)
    name = Column(String(500), nullable=False,index= True,unique=True)
    
    students = relationship("Student", back_populates="department")  

