from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic
from typing import Annotated
from app.models import *
from app.schemas import CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task was not found"
        )
    return task


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, create_task: CreateTask):
    user_test = db.scalar(select(User).where(User.id == user_id))
    if user_test is None:
        raise HTTPException(
            status_code=404,
            detail="User was not found"
        )
    db.execute(insert(Task).values(title=create_task.title,
                                   content=create_task.content,
                                   priority=create_task.priority,
                                   user_id=create_task.user,
                                   slug=slugify(create_task.title)
                                   ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task was not found"
        )
    db.execute(update(Task).where(Task.id == task_id).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Task update is successful!'}


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task was not found"
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Task delete is successful!'}
