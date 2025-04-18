from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    name : str
    email : EmailStr
    student_class : str 
    department_id: int

class StudentOut(StudentBase):
    id : int
    name : str 
    email: str
    student_class : str
    department_id: int
    class Config:
        form_attributes = True
