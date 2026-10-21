# To-Do List App

A simple command-line To-Do List application built using Python. It helps users manage daily tasks and saves them locally so they remain available after restarting the application.

## Features

- Add new tasks
- View pending tasks
- Mark tasks as completed
- View completed tasks separately
- Undo completed tasks and move them back to pending
- Edit existing tasks
- Delete pending tasks with confirmation
- Save tasks using JSON file storage
- Handle invalid task-number inputs
- Handle JSON and file errors
- Prevent empty tasks from being added
- Preserve tasks after restarting the application

## Technologies Used

- Python
- JSON
- File Handling
- Exception Handling

## How to Run

1. Install Python on your computer.
2. Clone or download this repository.
3. Open the project folder in your terminal.
4. Run the following command:

```bash
python todo.py
```

## Project Structure

- `todo.py` — Main application
- `tasks.json` — Local file used to store tasks (created when the app saves data)
- `tasks_backup.json` — Local backup file, if present

**Note:** Task data and backup files are excluded from GitHub using `.gitignore`.

## Author

Ayush Raj

GitHub: [https://github.com/ayushraj25-git](https://github.com/ayushraj25-git)

## Future Improvements

- Add task priorities
- Add due dates and reminders
- Build a graphical user interface
