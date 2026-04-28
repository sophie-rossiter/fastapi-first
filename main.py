from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    done: bool | None = False

tasks = []

app = FastAPI()

@app.post("/tasks/")
def add_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    current_task = tasks[id]
    return current_task