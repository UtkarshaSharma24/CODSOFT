#  TO-DO-LISTS

 
import json
import os

# File to  store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    #Load tasks from a file
   if os.path.exists(TASKS_FILE):
       with open(TASKS_FILE, 'r') as file:
           return json.load(file)
       return []
   
   
def save_tasks(tasks):
    #Save tasks to a file.
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
        
def add_task(tasks, title, description, due_date):
    #Add a new task.
    tasks.append ({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully!")
    
def view_tasks(tasks):
    #View all tasks.
    if not tasks:
        print("No tasks available")
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"]  else "Incomplete"
            print("{idx}.{task['title]} - Due: {task[''due_date]} - Status: {status}")
            print("Description: {task['description']}")
            
def update_task(task, task_id, title, description, due_date):
    #Update an existing task.
    if 0  <= task_id < len(tasks):
        tasks[task_id]["title"] = title
        tasks[task_id]["description"] = description
        tasks[task_id]["due_date"] = due_date
        save_tasks(task)
        print("Task updated successfully!")
    else:
        print("Invalid task ID.")
        
def delete_task(tasks, task_id):
    #Delete a task
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task ID.")
        
def mark_task_completed(tasks, task_id):
    #Mark a task as completed.
    if 0  <= task_id < len(tasks):
        tasks[task_id]["completed"] =  True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task ID.")
        
def main():
    task = load_tasks()
    
    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. View Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")       
        
        choice  = input("Choose an option:")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(task, title, description, due_date)
        elif choice == '2':
            view_tasks(task)
        elif choice == '3':
            task_id = int(input("Enter task ID to update: ")) - 1
            title = input("Enter updated task title: ")
            description = input("Enter updated task description: ")
            due_date = input("Enter updated due date (YYYY-MM-DD): ")
            update_task(task, task_id, title, description, due_date)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: ")) -  1
            delete_task(task, task_id)
        elif  choice == '5':
            task_id = int(input("Enter task ID to mark as completed: ")) - 1
            mark_task_completed(task, task_id)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if  __name__ == "__main__" : 
    main()         
        