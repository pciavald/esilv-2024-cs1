from pydantic import BaseModel
from typing import Optional
import json
import datetime
import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

@app.get("/", response_class=HTMLResponse)
def get_index():
  with open('index.html', 'r') as file:
    return file.read()    

class Task(BaseModel):
  id: Optional[int] = -1
  title: str
  added_date: Optional[str] = None
  done: Optional[bool] = False

class TaskList(BaseModel):
  tasks: list[Task]

def get_task_list_from_file():
  try:
    with open('data.json', 'r') as file:
      contents = json.loads(file.read())
      tasks = contents['tasks']
      task_list = TaskList(tasks=tasks)
  except Exception as e:
    task_list = TaskList(tasks=[])
  return task_list

def write_task_list(task_list):
  with open('data.json', 'w+') as file:
    file.write(task_list.model_dump_json(indent=2))

@app.post("/task", status_code=201)
async def add_task(task: Task) -> Task:
  task.added_date = str(datetime.datetime.now().timestamp())
  task_list = get_task_list_from_file()

  if len(task_list.tasks) > 0:
    task.id = task_list.tasks[-1].id + 1
  else:
    task.id = 1

  task_list.tasks.append(task)
  write_task_list(task_list)
  return task

@app.get("/task/list", status_code=200)
def get_tasks() -> TaskList:
  task_list = get_task_list_from_file()
  return task_list

@app.delete("/task/{id}", status_code=204)
def delete_task(id: int):
  task_list = get_task_list_from_file()
  for index, task in enumerate(task_list.tasks):
    if task.id == id:
      task_list.tasks.pop(index)
      write_task_list(task_list)
      return
  raise HTTPException(status_code=404)

class TaskEdit(BaseModel):
  id: int
  new_title: Optional[str] = None
  new_done: Optional[bool] = None

@app.put("/task", status_code=201)
def edit_task(edit: TaskEdit):
  task_list = get_task_list_from_file()
  for index, task in enumerate(task_list.tasks):
    if task.id == edit.id:
      if edit.new_title != None:
        task.title = edit.new_title
      if edit.new_done != None:
        task.done = edit.new_done
      write_task_list(task_list)
      return task
  raise HTTPException(status_code=404)
