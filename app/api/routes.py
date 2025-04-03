from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.tasks.example_task import example_background_task

router = APIRouter()


@router.get("/example")
async def example_endpoint():
    return {"message": "This is an example endpoint"}


@router.post("/tasks/example")
async def run_task():
    task = example_background_task.delay()
    return {"task_id": task.id, "status": "Task started"}