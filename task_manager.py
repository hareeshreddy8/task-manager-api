#Creates task object with default status (not completed)
def create_task(task_name,priority,due_date):
    return {"name":task_name,"status":False,"priority":priority,"due_date":due_date}
    

#Mark task as done using its index
def mark_task_done(tasks,index):
    if not tasks:
        return {"status" : "error","message":"No task available. ","data" : None}
    if not isinstance(index,int):
        return {"status" : "error","message":"Index must be an integer. ","data" : None}
    if not 0 <= index < len(tasks):
        return {"status" : "error","message":"Index out of range. ","data" :  None}
    #update task with that index  
    if tasks[index]["status"]:
        return {"status" : "error","message":"Task already completed. ","data" : tasks[index]}
    
    tasks[index]["status"] = True
    return {"status" : "success",
            "message":"Task updated successfully",
            "data" : tasks[index]}


#Delete task using its index
def delete_task(tasks,index):
    #validating tasks
    if not tasks :
        return {"status" : "error","message":"No task available. ","data" : None}
    #validating index type
    if not isinstance(index,int):
        return {"status" : "error","message":"Index must be in numbers ","data" : None}
    #validating index range
    if not 0 <= index < len(tasks) :
        return {"status" : "error","message":"Index out of range.  ","data" : None}
    #update tasks by deleting using its index 
    deleted_task= tasks.pop(index)

    return {"status": "success","message": "Task deleted successfully.","data": deleted_task}

#Edit name of existing task using index
def edit_task(tasks,index : int,new_name:str):
    if not tasks:
        return {"status" : "error","message":"No tasks available.","data": None}
    if not 0 <= index < len(tasks) :
        return {"status" : "error","message":"Index out of range.","data": None}
    if not new_name or not new_name.strip():
        return {"status" : "error","message":"Invalid name.","data": None}
    new_name = new_name.strip()
    if tasks[index]["name"] == new_name:
        return {"status" : "error","message":"Name must be new. ","data": None}
    tasks[index]["name"] = new_name
    return {"status" : "success","message":"Task name updated successfully.","data": tasks[index]}



#Search tasks with task name 
def search_task(tasks,name):
    tasks_found = []
    if not tasks:
        return {"status": "success","message": "No matching tasks found","data": []}
    if not name or not name.strip():
        return {"status": "error","message": "Invalid name.","data": None}
    name = name.strip().lower()
    for task in tasks:
        if name in task["name"].lower():
            tasks_found.append(task)
    return {"status": "success","message": "Tasks found successfully","data": tasks_found}


#filter task with priority 
def filter_tasks_by_priority(tasks,priority):
    filtered_tasks = []
    priority = priority.lower()
    for task in tasks:
        if task.get("priority") == priority.lower():
            filtered_tasks.append(task)

    return filtered_tasks

#sort tasks by duedate
def sort_tasks_by_due_date(tasks):
    return sorted(tasks,key = lambda x: x.get("due_date","9999-12-31"))

#sorting by priority
def sort_tasks_by_priority(tasks):
    priority_order = {"high" : 1,"medium": 2,"low":3}
    return sorted(tasks, key = lambda x : priority_order.get(x.get("priority").lower(),99))


#To get status of tasks
def get_task_stats(tasks):
    stats = {}
    for task in tasks:
        stats["total"] = stats.get("total",0) + 1
        if task.get("status"):
            stats["completed"] = stats.get("completed",0) + 1

        else :
            stats["pending"] = stats.get("pending",0) + 1

        priority = task.get("priority")

        stats[priority] = stats.get(priority,0) + 1

    return stats

#implementing function without input() and print() only structured response
def add_task(tasks,name,priority,due_date):
    #validating name 
    if not name or not name.strip():
        return {"status": "error","message":"Invalid name.","data":None}
    priority = priority.lower()
    if priority not in {"high","medium","low"}:
        return {"status": "error","message":"Invalid priority.","data":None}
    parts = due_date.split("-") 
    if len(parts) != 3:
        return {"status": "error","message":"Invalid duedate. must be in the format YYYY-MM-DD. ","data":None}
    year,month,day = parts
    
    if not(year.isdigit() and month.isdigit() and day.isdigit()):
        return {"status": "error","message":"Date must contain only numbers. ","data":None}
    
    if not(len(year) == 4 and len(month) == 2 and len(day) == 2) :
        return {"status": "error","message":"Invalid date format. ","data":None}
    
    month = int(month)
    day = int(day)
    
    if not (0 < month <= 12 and 0 < day <= 31):
        return {"status": "error","message":"Invalid month or day ","data":None}
    
    task = create_task(name,priority,due_date)
    tasks.append(task)

    return {"status": "success","message":"Task created successfully. ","data":tasks}
        
            
        
        
        


