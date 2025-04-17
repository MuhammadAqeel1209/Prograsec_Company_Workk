from pydantic import EmailStr
from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.student_schemas import StudentBase
from repository.student_repository import StudentRepository

class StudentService:
    def __init__(self, db: Session):
        self.repo = StudentRepository(db)

    def get_students_services(self):
        return self.repo.get_all_repository()

    def get_student_by_id_services(self, student_id: int):
        return self.repo.get_by_id_repository(student_id)

    def create_student_services(self, student: StudentBase):
        existing = self.repo.get_by_email_repository(student.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")
        return self.repo.create_user_repository(student)

    def update_student_services(self, student_email: EmailStr, student: StudentBase):
        student_with_email = self.repo.get_by_email_repository(student.email)
        if student_with_email:
            raise HTTPException(status_code=400, detail="Email already in use by another student")
        return self.repo.update_user_repository(student_email, student)

    def delete_student_services(self, student_email: EmailStr):
        return self.repo.delete_user_repository(student_email)
