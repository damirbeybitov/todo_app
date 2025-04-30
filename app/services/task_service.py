from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.crud.crud_task import task_crud

class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task_data: TaskCreate) -> Task:
        # You could add more complex business logic here if needed
        return task_crud.create(self.db, obj_in=task_data)

    def update_task(self, task_id: int, task_data: TaskUpdate) -> Task:
        task = task_crud.get(self.db, id=task_id)
        if not task:
            raise ValueError("Task not found")

        return task_crud.update(self.db, db_obj=task, obj_in=task_data)

    def delete_task(self, task_id: int) -> Task:
        return task_crud.remove(self.db, id=task_id)

    def list_tasks(self) -> list[Task]:
        return task_crud.get_multi(self.db)
