#Creates task object with default status (not completed)
def create_task(task_name,priority,due_date):
    return {"name":task_name,"status":False,"priority":priority,"due_date":due_date}
    

#Mark task as done using its index
def mark_task_done(task_id,update_task):
    
    #update task with that taskid in the database
     
    updated_task = update_task(task_id)
    
    if not updated_task:
        return None,"Task not found"
    return updated_task,None


#Delete task using its index
def delete_task(task_id,delete_task):
    #deleting task in database
    deleted_task = delete_task(task_id)
    if not deleted_task:
        return None,"Task not found"
    return deleted_task,None

#Edit name of existing task using index
def edit_task(task_id : int,new_name:str,edit_data_name):
    if not new_name or not new_name.strip():
        return None,("Invalid task name. ",400)
    
    result = edit_data_name(task_id,new_name)

    if not result :
        return None,("Task not found",404)
    
    return result,None
    
    


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


#filter tasks with priority or status 
def filter_tasks(priority,status,filter_data):
    if priority:
        priority = priority.lower()
    if not  priority or priority in {"high","low","medium"}:
        return None,("Invalid priority",400)
    filtered_tasks = filter_data(priority,status)
    
    if not filtered_tasks:
        return None,("No tasks found",404)
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
def add_task(task,insert_task):
    #validating name 
    if not task.name.strip():
        return None,"Task name cannot br empty"
    task.priority = task.priority.lower()
    if task.priority not in {"high","medium","low"}:
        return None,"Invalid priority."
    #DB
    insert_task(task.name,task.priority,task.due_date)

    return {
        "name": task.name,
        "priority": task.priority,
        "due_date": task.due_date,
        "status": False
    },None
        
            
        
        
        


