
import json
import os

FILE_NAME = "tasks.json"

data_error = False

# Load saved tasks
if os.path.exists(FILE_NAME):
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            tasks = data
            completed_tasks = []

        elif isinstance(data, dict):
            tasks = data.get("tasks", [])
            completed_tasks = data.get("completed_tasks", [])

            if not isinstance(tasks, list) or not isinstance(completed_tasks, list):
                raise ValueError("Invalid task data format")

        else:
            raise ValueError("Invalid JSON data format")

    except (json.JSONDecodeError, ValueError) as e:
        print("Error loading tasks:", e)
        data_error = True
        tasks = []
        completed_tasks = []

    except OSError as e:
        print("File error:", e)
        data_error = True
        tasks = []
        completed_tasks = []

else:
    tasks = []
    completed_tasks = []


# Save tasks to file
def save_tasks():
    if data_error:
        print("Cannot save: tasks.json has a data error.")
        return False

    data = {
        "tasks": tasks,
        "completed_tasks": completed_tasks
    }

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
        return True

    except OSError as e:
        print("Error saving tasks:", e)
        return False


# Main app
while True:
    print("\n---- TO-DO LIST APP ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("4. Complete Task")
    print("5. View Completed Tasks")
    print("6. Edit Task")
    print("7. Delete Task")
    print("8. Undo Completed Task")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")

        if task.strip() == "":
            print("Task cannot be empty!")

        elif data_error:
            print("Task was not added because the data file has an error.")

        else:
            tasks.append(task)

            if save_tasks():
                print("Task added successfully!")
            else:
                tasks.pop()

    # View Pending Tasks
    elif choice == "2":
        if not tasks:
            print("No pending tasks.")
        else:
            print("\nYour Pending Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Exit
    elif choice == "3":
        print("App closed.")
        break

    # Complete Task
    elif choice == "4":
        if data_error:
            print("Cannot modify tasks because the data file has an error.")
        elif not tasks:
            print("No pending tasks.")
        else:
            print("\nYour Pending Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_no = int(input("Enter task number to complete: "))

                if 1 <= task_no <= len(tasks):
                    completed_task = tasks.pop(task_no - 1)
                    completed_tasks.append(completed_task)

                    if save_tasks():
                        print("Completed:", completed_task)
                    else:
                        completed_tasks.pop()
                        tasks.insert(task_no - 1, completed_task)
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    # View Completed Tasks
    elif choice == "5":
        if not completed_tasks:
            print("No completed tasks.")
        else:
            print("\nYour Completed Tasks:")
            for i, task in enumerate(completed_tasks, start=1):
                print(f"{i}. {task}")

    # Edit Task
    elif choice == "6":
        if data_error:
            print("Cannot modify tasks because the data file has an error.")
        elif not tasks:
            print("No pending tasks.")
        else:
            print("\nYour Pending Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_no = int(input("Enter task number to edit: "))

                if 1 <= task_no <= len(tasks):
                    new_task = input("Enter new task name: ")

                    if new_task.strip() == "":
                        print("Task cannot be empty!")
                    else:
                        old_task = tasks[task_no - 1]
                        tasks[task_no - 1] = new_task

                        if save_tasks():
                            print("Task updated successfully!")
                        else:
                            tasks[task_no - 1] = old_task
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    # Delete Task
    elif choice == "7":
        if data_error:
            print("Cannot modify tasks because the data file has an error.")
        elif not tasks:
            print("No pending tasks.")
        else:
            print("\nYour Pending Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_no = int(input("Enter task number to delete: "))

                if 1 <= task_no <= len(tasks):
                    confirm = input(
                        "Are you sure you want to delete this task? (y/n): "
                    ).strip().lower()

                    if confirm == "y":
                        deleted_task = tasks.pop(task_no - 1)

                        if save_tasks():
                            print("Deleted:", deleted_task)
                        else:
                            tasks.insert(task_no - 1, deleted_task)
                    else:
                        print("Deletion cancelled.")

                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    # Undo Completed Task
    elif choice == "8":
        if data_error:
            print("Cannot modify tasks because the data file has an error.")
        elif not completed_tasks:
            print("No completed tasks to undo.")
        else:
            print("\nYour Completed Tasks:")
            for i, task in enumerate(completed_tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_no = int(input("Enter task number to undo: "))

                if 1 <= task_no <= len(completed_tasks):
                    task = completed_tasks.pop(task_no - 1)
                    tasks.append(task)

                    if save_tasks():
                        print("Task moved back to pending:", task)
                    else:
                        tasks.pop()
                        completed_tasks.insert(task_no - 1, task)
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    else:
        print("Invalid choice!")




