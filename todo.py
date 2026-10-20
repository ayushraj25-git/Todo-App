
import json
import os

FILE_NAME = "tasks.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    if isinstance(data, list):
        tasks = data
        completed_tasks = []
    else:
        tasks = data.get("tasks", [])
        completed_tasks = data.get("completed_tasks", [])

else:
    tasks = []
    completed_tasks = []


def save_tasks():
    data = {
        "tasks": tasks,
        "completed_tasks": completed_tasks
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


while True:
    print("\n---- TO-DO LIST APP ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("4. Complete Task")
    print("5. View Completed Tasks")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")

        if task.strip() == "":
            print("Task cannot be empty!")
        else:
            tasks.append(task)
            save_tasks()
            print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No pending tasks.")
        else:
            print("\nYour Pending Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("App closed.")
        break

    elif choice == "4":
        if not tasks:
            print("No pending tasks.")
        else:
            print("\nYour Pending Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_no = int(
                    input("Enter task number to complete: ")
                )

                if 1 <= task_no <= len(tasks):
                    completed_task = tasks.pop(task_no - 1)
                    completed_tasks.append(completed_task)

                    save_tasks()

                    print("Completed:", completed_task)
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "5":
        if not completed_tasks:
            print("No completed tasks.")
        else:
            print("\nYour Completed Tasks:")

            for i, task in enumerate(completed_tasks, start=1):
                print(f"{i}. {task}")

    else:
        print("Invalid choice!")



