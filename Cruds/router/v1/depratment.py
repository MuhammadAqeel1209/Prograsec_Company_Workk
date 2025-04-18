from fastapi import APIRouter, Depends, HTTPException, status
from schemas.department_schemas import DepartmentInput,DepartmentOutput
from services.depratment_services import DepartmentService
from config.database import get_db
from sqlalchemy.orm import Session



router = APIRouter(prefix="/department", tags=["Department"])

def get_depratment_service(db: Session = Depends(get_db)):
    return DepartmentService(db)
@router.get("/", response_model=list[DepartmentOutput], status_code=status.HTTP_200_OK)
def get_depratments(service: DepartmentService = Depends(get_depratment_service)):
    return service.get_all_departments_services()

@router.get("/{depratment_name}", response_model=DepartmentOutput, status_code=status.HTTP_200_OK)
def get_depratment(depratment_name: str, service: DepartmentService = Depends(get_depratment_service)):
    depratment = service.get_department_by_name(depratment_name)
    if not depratment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="depratment not found")
    return depratment

@router.post("/", response_model=DepartmentOutput, status_code=status.HTTP_201_CREATED)
def create_depratment(depratment: DepartmentInput, service: DepartmentService = Depends(get_depratment_service)):
    created = service.create_department_services(depratment)
    if not created:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")
    return created

@router.put("/{depratment_id}", response_model=DepartmentOutput, status_code=status.HTTP_200_OK)
def update_depratment(depratment_id: int, depratment: DepartmentInput, service: DepartmentService = Depends(get_depratment_service)):
    updated = service.update_department_services(depratment_id, depratment)
    if not updated:
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="depratment not found")
    return updated

@router.delete("/{depratment_id}", status_code=status.HTTP_200_OK)
def delete_depratment(depratment_id: int, service: DepartmentInput = Depends(get_depratment_service)):
    deleted = service.delete_department_services(depratment_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="depratment not found")
    return {"message": "depratment deleted successfully"}
