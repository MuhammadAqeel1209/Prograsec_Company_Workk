from fastapi import APIRouter
from router.v1 import student
from router.v1 import depratment


api_router = APIRouter()
api_router.include_router(student.router)
api_router.include_router(depratment.router)

