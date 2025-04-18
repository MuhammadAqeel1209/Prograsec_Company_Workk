from fastapi import APIRouter, Depends, HTTPException, status
from schemas.student_schemas import StudentBase, StudentOut
from services.student_service import StudentService
from config.database import get_db
from sqlalchemy.orm import Session
from pydantic import EmailStr


router = APIRouter(prefix="/student", tags=["Student"])
def get_student_service(db: Session = Depends(get_db)) -> StudentService:
    
    return StudentService(db)

@router.get("/", response_model=list[StudentOut], status_code=status.HTTP_200_OK)
def get_students(service: StudentService = Depends(get_student_service)):
    return service.get_students_services()

@router.get("/{student_id}", response_model=StudentOut, status_code=status.HTTP_200_OK)
def get_student(student_id: int, service: StudentService = Depends(get_student_service)):
    student = service.get_student_by_id_services(student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

@router.post("/", response_model=StudentOut, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentBase, service: StudentService = Depends(get_student_service)):
    created = service.create_student_services(student)
    if not created:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")
    return created

@router.put("/{student_email}", response_model=StudentOut, status_code=status.HTTP_200_OK)
def update_student(student_email: EmailStr, student: StudentBase, service: StudentService = Depends(get_student_service)):
    updated = service.update_student_services(student_email, student)
    if not updated:
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return updated

@router.delete("/{student_email}", status_code=status.HTTP_200_OK)
def delete_student(student_email: EmailStr, service: StudentService = Depends(get_student_service)):
    deleted = service.delete_student_services(student_email)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return {"message": "Student deleted successfully"}
