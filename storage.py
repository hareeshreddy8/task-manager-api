import json
FILE_NAME = "tasks.json"
def load_tasks():
    try :
        with open(FILE_NAME,"r") as file :
            tasks = json.load(file)
            for task in tasks :
                if "status" not in task:
                    task["status"] = False

                if "name" not in task :
                    task["name"] = "Untitiled Task"

            return tasks
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        #resetting data
        tasks = []
        save_tasks(tasks)
        return tasks
    

#to save the contents in memory to file to not lose them
def save_tasks(tasks):
    with open(FILE_NAME,"w") as file :
        json.dump(tasks,file)
