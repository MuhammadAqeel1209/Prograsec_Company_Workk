from sqlalchemy.orm import Session
from models.department import Department
from schemas.department_schemas import DepartmentInput

class Department_Repository:
    def __init__(self,db:Session):
        self.db = db
        
    def get_all_department_repository(self):
        return self.db.query(Department).all()

    def get_department_repository(self, dept_name: str):
        return self.db.query(Department).filter(Department.name == dept_name).first()
    
    def get_department_repository_id(self, dept_id: int):
        return self.db.query(Department).filter(Department.id == dept_id).first()

    def create_department(self, department: DepartmentInput):
        db_dept = Department(name=department.name)
        self.db.add(db_dept)
        self.db.commit()
        self.db.refresh(db_dept)
        return db_dept

    def update_department_repository(self, dept_id: int, department: DepartmentInput):
        db_dept = self.get_department_repository_id(dept_id)
        if db_dept:
            db_dept.name = department.name
            self.db.commit()
            self.db.refresh(db_dept)
        return db_dept

    def delete_department_repository(self, dept_id: int):
        db_dept = self.get_department_repository_id(dept_id)
        if db_dept:
            self.db.delete(db_dept)
            self.db.commit()
        return db_dept
