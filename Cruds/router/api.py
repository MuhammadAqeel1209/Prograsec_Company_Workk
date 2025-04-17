from fastapi import APIRouter
from router.v1 import student


api_router = APIRouter()
api_router.include_router(student.router)

