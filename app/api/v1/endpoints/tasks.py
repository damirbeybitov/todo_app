from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter()

# Dependency injection
def get_task_service() -> TaskService:
    return TaskService()

@router.get("/{chat_id}", response_model=List[TaskRead])
def get_all_tasks(chat_id: int, service: TaskService = Depends(get_task_service)):
    return service.get_tasks(chat_id)

@router.get("/{chat_id}/{task_id}", response_model=TaskRead)
def get_task(chat_id: int, task_id: int, service: TaskService = Depends(get_task_service)):
    task = service.get_task(chat_id, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/{chat_id}/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(chat_id: int, task: TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.create_task(task)

@router.put("/{chat_id}/{task_id}", response_model=TaskRead)
def update_task(chat_id: int, task_id: int, task_data: TaskUpdate, service: TaskService = Depends(get_task_service)):
    updated = service.update_task(chat_id, task_id, task_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{chat_id}/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(chat_id: int, task_id: int, service: TaskService = Depends(get_task_service)):
    success = service.delete_task(chat_id, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
