from typing import Optional,List
from pydantic import BaseModel
from task_manager import add_task,mark_task_done,delete_task
from storage import load_tasks,save_tasks
from fastapi import FastAPI


app = FastAPI()

class TaskCreate(BaseModel):
    name : str
    priority : str
    due_date : str

class Task(BaseModel):
    name : str
    priority : Optional[str] = None
    due_date : Optional[str] = None
    status : bool

class TaskResponse(BaseModel):
    status : str
    message : str
    data : Optional[Task] = None

class TaskListResponse(BaseModel):
    status : str
    message : str
    data : List[Task]


tasks = load_tasks()
#health check
@app.get("/")
def home():
    return {"message": "API is running"}

#create task
@app.post("/tasks",response_model=TaskResponse)
def create_task_api(task : TaskCreate):
    response = add_task(tasks, task.name, task.priority, task.due_date)
    save_tasks(tasks)
    return response

@app.get("/tasks",response_model=TaskListResponse)
def get_tasks_api():
    return {"status": "success",
           "message": "Tasks fetched successfully",
            "data": tasks }

@app.put("/tasks/{index}",response_model=TaskResponse)
def mark_task_done_api(index:int):
    response = mark_task_done(tasks,index)
    save_tasks(tasks)
    return response 

@app.delete("/tasks/{index}",response_model=TaskResponse)
def delete_task_api(index:int):
    response = delete_task(tasks,index)
    save_tasks(tasks)
    return response 