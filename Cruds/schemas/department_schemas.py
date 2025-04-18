from pydantic import BaseModel

class DepartmentInput(BaseModel):
    name : str 
    
class DepartmentOutput(BaseModel):
    id : int
    name : str
    
    class Config:
        form_attributes = True