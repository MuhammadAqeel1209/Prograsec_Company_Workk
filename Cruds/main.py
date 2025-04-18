from fastapi import FastAPI
from router import api
from utills.init_db import create_tables


# Initialize FastAPI app
app = FastAPI(
    title="Student Management API",
    version="1.0.0"
)

create_tables()

# Include your API router
app.include_router(api.api_router, prefix="/api/v1")
