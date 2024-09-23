from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: str | None

class Task(STaskAdd):
    id: int

class STaskId(BaseModel):
    ok: bool = True
    task_id: int

