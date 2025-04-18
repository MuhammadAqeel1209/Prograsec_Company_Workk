from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.department_schemas import DepartmentInput,DepartmentOutput
from repository.department_repository import Department_Repository

class DepartmentService:
    def __init__(self, db: Session):
        self.repo = Department_Repository(db)

    def get_all_departments_services(self):
        return self.repo.get_all_department_repository()

    def get_department_by_name(self, department_name: str):
        department = self.repo.get_department_repository(department_name)
        if not department:
            raise HTTPException(status_code=404, detail="Department not found")
        return department

    def create_department_services(self, department: DepartmentInput):
        existing = self.repo.get_department_repository(department.name)
        if existing:
            raise HTTPException(status_code=400, detail="Department already exists")
        return self.repo.create_department(department)

    def update_department_services(self, department_id: int, department: DepartmentOutput):
        existing = self.repo.get_department_repository_id(department_id)
        if not existing:
            raise HTTPException(status_code=404, detail="Department not found")
        return self.repo.update_department_repository(department_id, department)

    def delete_department_services(self, department_id: int):
        existing = self.repo.get_department_repository_id(department_id)
        if not existing:
            raise HTTPException(status_code=404, detail="Department not found")
        return self.repo.delete_department_repository(department_id)
