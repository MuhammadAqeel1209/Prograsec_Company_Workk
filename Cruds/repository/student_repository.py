from pydantic import EmailStr
from sqlalchemy.orm import Session
from models.students import Student
from models.department import Department
from schemas.student_schemas import StudentBase
from fastapi import HTTPException, status

class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_repository(self):
        return self.db.query(Student).all()

    def get_by_id_repository(self, student_id: int):
        return self.db.query(Student).filter(Student.id == student_id).first()

    def get_by_email_repository(self, email: str):
        return self.db.query(Student).filter(Student.email == email).first()

    def create_user_repository(self, student: StudentBase):
        # Check if department exists
        department = self.db.query(Department).filter(Department.id == student.department_id).first()
        if not department:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Department with this ID does not exist"
            )
        
        db_student = Student(
            name=student.name,
            student_class=student.student_class,
            email=student.email,
            department_id=student.department_id
        )
        self.db.add(db_student)
        self.db.commit()
        self.db.refresh(db_student)
        return db_student

    def update_user_repository(self, student_email: EmailStr, student: StudentBase):
        db_student = self.get_by_email_repository(student_email)
        if not db_student:
            return None

        # Check if department exists
        department = self.db.query(Department).filter(Department.id == student.department_id).first()
        if not department:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Department with this ID does not exist"
            )

        db_student.name = student.name
        db_student.student_class = student.student_class
        db_student.email = student.email
        db_student.department_id = student.department_id
        self.db.commit()
        self.db.refresh(db_student)
        return db_student

    def delete_user_repository(self, student_email: EmailStr):
        db_student = self.get_by_email_repository(student_email)
        if db_student:
            self.db.delete(db_student)
            self.db.commit()
        return db_student
