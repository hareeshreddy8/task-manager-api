# CLI Productivity Tracker(phase 1 - In memory version)
#--------------------------------------------------------
#Features :
#1.Add task
#2.Display Task
#3.Marks tasks as completed 
#4.File persistent(using JSON)
#5.Delete task
#6.Edit task
#7.Fault tolerance(JSONDecodeError)
#--------------------------------------------------------

from storage import load_tasks as load_tasks, save_tasks as save_tasks
import task_manager

#Display all tasks with their index and completion status
def display_tasks(tasks):
    if not tasks:
        print("No tasks to display")
        return
    for index,task in enumerate(tasks):
        priority = task.get("priority","N/A")
        due_date = task.get("due_date","N/A")
        if not task["status"]:
            print(f"{index}. {task['name']} [ ] ({priority},{due_date})")

        else :
            print(f"{index}. {task['name']} [✔] ({priority},{due_date})")
                  
    
                  

#Get a valid task index from the user with proper validation
def index_of_task(tasks):
    while True:
        try:
            index = int(input("enter task number: "))
            if index >= len(tasks) or index < 0 :
                print(f"Invalid index,Please enter between {0} to {len(tasks) - 1}")
            
            else:
                return index
        except ValueError:
            print(f"Invalid input.Please enter a number.")


           
#creating menu for users to decide what they want to do
def main():
    tasks = load_tasks()
    while True :
        print("===== MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Edit Task Name")
        print("6. Search task by name")
        print("7. Filter with priority")
        print("8. Status of tasks")
        print("9. Exit")
        print("================")
        try :
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            print("Enter task name: ")
            task = input()
            while True:
                priority = input("set priority for the task: ")
                valid_priority = {"high","medium","low"}
                if priority.lower() in valid_priority:
                    break
                else :
                    print("Please select priority as high/medium/low")

            while True:
                due_date = input("enter the due date: ")
                parts = due_date.split("-")
                if len(parts) != 3 :
                    print("Invalid format. Use YYYY-MM-DD")
                    continue
                year , month , day = parts
                if not(year.isdigit() and month.isdigit() and day.isdigit()):
                    print("date must contain only numbers")
                    continue
                if not (len(year) == 4 and len(month) == 2 and len(day) == 2):
                    print("Invalid format. Use YYYY-MM-DD")

                month = int(month)
                day = int(day)

                if not (0 < month <= 12 and 0 < day <= 31 ) : 
                    print("Invalid month or day")
                    continue

                else :
                    break
            tasks.append(task_manager.create_task(task,priority,due_date))
            save_tasks(tasks)
            print("Task created successfully.")

        elif choice == 2:
            display_tasks(tasks)

        elif choice == 3:
            if not tasks :
                print("NO tasks available")
                continue
            try:
                index = index_of_task(tasks)
                task_manager.mark_task_done(tasks,index)
                save_tasks(tasks)
                print("Task marked as completed. Updated tasks:")
                display_tasks(tasks)
            except (ValueError,IndexError) as e :
                print(e)
            

        elif choice == 4 :
            if not tasks :
                print("NO tasks available")
                continue
            try :
                index = index_of_task(tasks)
                task_manager.delete_task(tasks,index)
                save_tasks(tasks)
                print("Task deleted successfully. Updated tasks: ")
                display_tasks(tasks)

            except (ValueError,IndexError) as e:
                print(e)
        elif choice == 5:
            if not tasks:
                print("No tasks available")
                continue
            try :
                index = index_of_task(tasks)
                while True :
                    new_name = str(input("Enter a new name to task: "))
                    if new_name.strip():
                        break
                    else :
                        print("Please enter valid name")
                task_manager.edit_task(tasks,index,new_name)
                save_tasks(tasks)
                print("Task name updated successfully. Updated tasks")
                display_tasks(tasks)

            except ValueError:
                print("Please enter a valid name.")
        elif choice == 6:
            
            while True:
                name = str(input("Enter task name to search: "))
                if name.strip():
                    break
                else :
                    print("Please enter a valid name. ")
            tasks_found = task_manager.search_task(tasks,name)
            if len(tasks_found) != 0:
                display_tasks(tasks_found)

            else :
                print("No matches found")
        elif choice == 7:
            while True:
                priority = input("Enter priority to filter tasks: ")
                if priority.lower() in {"high","medium","low"}:
                    break 
                else :
                    print("Invalid priority. Choose: high/medium/low")

            filtered_tasks = task_manager.filter_tasks_by_priority(tasks,priority)
            if filtered_tasks:
                display_tasks(filtered_tasks)
            else :
                print("No tasks found with that priority")

        elif choice == 8:
            stats = task_manager.get_task_stats(tasks)
            if stats:
                print("===== DASHBOARD =====")
                print(f"Total tasks   : {stats.get('total', 0)}")
                print(f"Completed     : {stats.get('completed', 0)}")
                print(f"Pending       : {stats.get('pending', 0)}")
                print(f"High priority : {stats.get('high', 0)}")
                print(f"Medium        : {stats.get('medium', 0)}")
                print(f"Low           : {stats.get('low', 0)}")
                print("=====================")

            else :
                print("No tasks to show status. ")

        elif choice == 9:
            break
        else :
            print("Invalid choice. Please try again.")


#using __name__ check 

if __name__ == "__main__" :
    main()

    