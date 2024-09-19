from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def hello():
#   return {"message": "Hello World"}

from pydantic import BaseModel
from typing import Optional
import json
import datetime

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

from fastapi.responses import HTMLResponse
@app.get("/", response_class=HTMLResponse)
def get_index():
  with open('index.html', 'r') as file:
    return file.read()    

class Task(BaseModel):
  title: str
  added_date: Optional[str] = None

class TaskList(BaseModel):
  tasks: list[Task]

@app.post("/todo")
async def add_todo(task: Task):

  task.added_date = str(datetime.datetime.now().timestamp())

  try:
    with open('data.json', 'r') as file:
      contents = json.loads(file.read())
      tasks = contents['tasks']
      task_list = TaskList(tasks=tasks)
  except Exception as e:
    task_list = TaskList(tasks=[])

  task_list.tasks.append(task)
  with open('data.json', 'w+') as file:
    file.write(task_list.model_dump_json(indent=2))
  return 'OK'

@app.get("/todos")
def get_todos() -> TaskList:
  try:
    with open('data.json', 'r') as file:
      contents = file.read()
      tasks = json.loads(contents)['tasks']
  except Exception as e:
    tasks = []
  return TaskList(tasks=tasks)
