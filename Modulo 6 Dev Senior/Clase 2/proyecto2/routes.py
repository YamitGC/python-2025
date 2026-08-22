from fastapi import APIRouter, HTTPException
from models import Task
from data import tasks_db, contador_id

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Bienvenido a la API de Tareas"}

@router.get("/tasks")
def get_tasks():
    return tasks_db

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return {"message": "Task found", "task": task}
    raise HTTPException(status_code=404, detail="Task not found")

@router.post("/tasks/")
def create_task(task: Task):
    global contador_id
    task.id = contador_id
    tasks_db.append(task)
    contador_id += 1
    return {"message": "Task created", "task": task}

@router.put("/tasks/{task_id}")
def update_task(task_id: int, update_task: Task):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[index] = update_task
            update_task.id = task_id
            return {"message": "Task updated", "task": update_task}
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            deleted_task = tasks_db.pop(index)
            return {"message": "Task deleted", "task": deleted_task}
    raise HTTPException(status_code=404, detail="Task not found")
