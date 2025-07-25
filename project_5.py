# todo list item 1: complete/incomplete

#load exsisting item

# create a new item
# list items 
# mark item as complete 
# save items 

import json

file_name = 'todo_list.json'

def load_tasks():
    try:
        with open (file_name, 'r') as file:
            return json.load(file)
    except:
        return {"tasks": []}
    

def save_tasks(tasks):
    try:
        with open(file_name, 'w') as file:
            json.dump(tasks, file, indent=4)
    except:
        print("Failed to save tasks.")


def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks available.")
    else:
        print("Your to do list: ")
        for idx,  task in enumerate(task_list):
            status = "[Complete]" if task["completed"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")
            
        

def create_tasks(tasks):
    description = input("Enter task description: ").strip()
    if description:
        tasks['tasks'].append({"description": description, "completed": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task description cannot be empty.")
        
    

def mark_task_complete(tasks):
    view_tasks(tasks)
    task_list = tasks["tasks"]
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(task_list):
            task_list[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number. Please try again.")    
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            create_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid option, please try again.")

