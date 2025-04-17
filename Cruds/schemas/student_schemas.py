from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    name : str
    email : EmailStr
    student_class : str 

class StudentOut(StudentBase):
    id : int
    name : str 
    email: str
    student_class : str
    class Config:
        form_attributes = True
