from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    done: bool | None = False

tasks = []

app = FastAPI()

@app.post("/tasks/")
def add_task(task: Task):
    '''Creates a new task and adds it to the task list'''
    tasks.append(task)
    return task

@app.get("/tasks")
def get_tasks():
    """Returns all tasks currently in the task list"""
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    """Returns a single task by it's position in the task list"""
    current_task = tasks[id]
    return current_task