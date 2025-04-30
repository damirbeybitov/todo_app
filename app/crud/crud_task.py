# app/crud/crud_user.py
from app.crud.base import CRUDBase
from app.models.task import User
from app.schemas.task import TaskCreate, TaskUpdate

class CRUDTask(CRUDBase[User, TaskCreate, TaskUpdate]):
    pass

task_crud = CRUDTask(User)
