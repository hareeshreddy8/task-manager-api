from typing import Optional,List
from pydantic import BaseModel
from datetime import date
import task_manager 
from storage import load_tasks,save_tasks
from fastapi import FastAPI,HTTPException
import database 

database.create_table()
app = FastAPI()

class TaskCreate(BaseModel):
    name : str
    priority : str
    due_date : date

class Task(BaseModel):
    id : int
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

class UpdateName(BaseModel):
    name : str


tasks = load_tasks()
#health check
@app.get("/")
def home():
    return {"message": "API is running"}

#create task
@app.post("/tasks",status_code=201)
def create_task_api(task : TaskCreate):
    result , error = task_manager.add_task(task,database.insert_task)
    if error:
        msg,code = error
        raise HTTPException(status_code=code,detail=msg)
    return {"message": "Task created successfully",
            "data": result
    }

@app.get("/tasks",status_code=200)
def get_tasks_api():
    tasks = database.get_all_tasks()
    return {"message": "Tasks fetched successfully",
            "data": tasks }

@app.put("/tasks/{task_id}",status_code=200)
def mark_task_done_api(task_id:int):
    updated_task,error = task_manager.mark_task_done(task_id,database.update_task_status)
    if error:
        raise HTTPException(status_code=404,detail = error)

    return {
        "message": "Task updated",
        "data": updated_task
    }


@app.delete("/tasks/{task_id}",status_code=200)
def delete_task_api(task_id:int):
    deleted_task,error = task_manager.delete_task(task_id,database.delete_data)
    if error :
        raise HTTPException(status_code=404,detail = error)
    return {"message": "Task deleted successfully",
            "data": deleted_task}
 
@app.patch("/tasks/{task_id}/name",status_code=200)
def edit_task_api(task_id:int,payload : UpdateName):
    edited_task,error = task_manager.edit_task(task_id,payload.name,database.edit_data_name)
    if error :
        message,code = error
        raise HTTPException(status_code=code,detail = message)
    
    return {
        "message": "Task name updated succesfully. ",
        "data": edited_task
    }

@app.get("/tasks/filter",status_code=200)
def filter_tasks_api(priority:Optional[str] = None,status:Optional[bool] = None):
    result,error = task_manager.filter_tasks(priority,status,database.filter_data)

    if error:
        message,code = error
        raise HTTPException(status_code=code,detail = message)
    
    return {
        "message": "tasks filtered successfully",
        "data" : result
    }

@app.get("/tasks/sort",status_code = 200)
def sort_tasks_api(by : str = "due_date"):

    result,error = task_manager.sort_tasks(by,database.sort_data)

    if error :
        msg , code = error

        raise HTTPException(status_code=code,detail = msg)
    
    return {
        "message": "Tasks sorted successfully.",
        "data" : result
    }

@app.get("/tasks/stats",status_code = 200)
def get_stats():
    result , error = task_manager.get_task_stats(database.data_stats)

    if error :
        msg,code = error 
        raise HTTPException(status_code=code,detail=msg)
    
    return result 