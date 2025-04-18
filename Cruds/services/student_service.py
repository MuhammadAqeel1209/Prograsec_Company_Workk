from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.student_schemas import StudentBase, EmailLogin
from repository.student_repository import StudentRepository
from utills.auth import verify_password, create_access_token

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

    def update_student_services(self, email: str, student: StudentBase):
        return self.repo.update_user_repository(email, student)

    def delete_student_services(self, email: str):
        return self.repo.delete_user_repository(email)

    def authenticate_student(self, login: EmailLogin):
        user = self.repo.get_by_email_repository(login.email)
        if not user or not verify_password(login.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token = create_access_token({"sub": user.email})
        return {"access_token": token, "token_type": "bearer"}
