'''*********** TASK ORGANIZER **************

* TITLE: Task Organizer
* AUTHOR: [JAMES_ALCON]
* DATE: 2026-01-26
* DESCRIPTION: Algorithm to organize tasks, where you can add, list, and complete tasks.
* CONCEPTS: - Lists to store tasks
            - Dictionaries to represent each task with id, description, and status
            
**************************************************'''


# Adds a new task with status 'Pending' and an incremental id.
def add_task(task_list, description):
    if task_list:
        new_id = task_list[-1]['id'] + 1
    else:
        new_id = 1
    task = {"id": new_id, "description": description, "status": "Pending"}
    task_list.append(task)
    print("Task added.")

# Shows all tasks or warns if the list is empty.
def list_tasks(task_list):
    if not task_list:
        print("The task list is empty.")
        return
    
    print("--- MY TASKS ---")
    for task in task_list:
        print(f"[{task['id']}] {task['description']} - ({task['status']})")

# Changes the task status from 'Pending' to 'Completed' by ID.
def complete_task(task_list, task_id):
    for task in task_list:
        if task['id'] == task_id:
            if task['status'] == "Pending":
                task['status'] = "Completed"
                print(f"Task {task_id} completed.")
            else:
                print(f"Task {task_id} is already completed.")
            return
    print(f"Task with ID {task_id} not found.")

# Program menu.
def menu():
    tasks = []
    while True:
        print("\n=== TO-DO LIST v1.0 ===")
        print("1. Add")
        print("2. List")
        print("3. Complete")
        print("0. Exit")
        option = input("Option: ").strip()

        if option == "1":
            description = input("Task description: ").strip()
            if description:
                add_task(tasks, description)
            else:
                print("Invalid description. Try again.")

        elif option == "2":
            list_tasks(tasks)

        elif option == "3":
            try:
                task_id = int(input("Task ID to complete: ").strip())
                complete_task(tasks, task_id)
            except ValueError:
                print("Invalid ID. Please enter an integer.")

        elif option == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Choose between 0 and 3.")

if __name__ == "__main__":
    menu()
