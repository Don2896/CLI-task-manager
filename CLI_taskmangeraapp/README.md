# CLI Task Manager (Python)

A command-line task management application built in Python to demonstrate object-oriented programming, data persistence, and clean modular application design.


## Overview
This project is a CLI-based task manager that allows users to create, view, complete, and delete tasks. It was built to reinforce core software engineering principles, particularly around structuring applications cleanly and handling persistent data.

The application simulates a simple backend system, where tasks are managed in memory and persisted to disk using JSON.


## Features
- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Persistent storage using JSON (data is retained between runs)
- Input validation for task IDs and task titles
- Automatic and consistent task ID generation


## Project Structure

```
CLI_taskmanager/
│
├── app/
│   ├── __init__.py
│   ├── task.py
│   ├── task_manager.py
│   ├── storage.py
│   
│
├── main.py
├── requirements.txt
└── README.md
└── tasks.json
```



## How it works
Tasks are represented as Python objects via the `Task` class. These objects are managed in memory by the `TaskManager`, which handles all operations such as adding, completing, and deleting tasks.

When the application saves data, each task is converted into a dictionary and written to a JSON file. When the application starts, the JSON file is read, converted into dictionaries, and then reconstructed back into `Task` objects.

This creates a full data cycle between in-memory objects and persistent storage.


## How to Run
Clone the repository and run the application from the project root:

bash
git clone https://github.com/yourusername/cli-task-manager.git
cd cli-task-manager
python main.py


## Example usage
=========================
      TASK MANAGER
=========================
1. View tasks
2. Add task
3. Complete task
4. Delete task
5. Exit

Choose an option: 2
Enter task title: Study Python OOP

Task added: [1] - Study Python OOP - incomplete
