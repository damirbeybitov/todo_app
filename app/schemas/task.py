from typing import Optional
from pydantic import BaseModel

class TaskCreate(BaseModel):
    task_description: str

class TaskRead(BaseModel):
    task_id: int
    task_description: str

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    task_description: Optional[str] = None

    class Config:
        orm_mode = True
