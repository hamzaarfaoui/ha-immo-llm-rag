from fastapi import FastAPI, APIRouter
import os


base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def index():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "message": f"Welcome to {app_name} {app_version}"
    }
