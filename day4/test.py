from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
  return {"message": "Hello World"}

from pydantic import BaseModel

class Task(BaseModel):
  title: str

@app.post("/task")
def add_todo(task: Task):
  print(task)
