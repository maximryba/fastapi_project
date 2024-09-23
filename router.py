from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from repository import TaskRepository
from schemas import STaskAdd, Task, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.post("/add")
async def add_one(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok" : True, "task_id" : task_id}

@router.get("/all")
async def get_all() -> list[Task]:
    tasks = await TaskRepository.find_all()
    return tasks
