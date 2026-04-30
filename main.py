from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    done: bool | None = False

tasks = []

app = FastAPI()

@app.post("/tasks/")
def add_task(task: Task):
    '''Accepts a Task in the request body, appends it to the task list, and returns the created task'''
    tasks.append(task)
    return task

@app.get("/tasks")
def get_tasks():
    """Responds to a GET request to /tasks by returning the tasks list"""
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    """Takes the task ID from the URL path, retrieves the corrosponding task from the task list and returns it"""
    current_task = tasks[id]
    return current_task