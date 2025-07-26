# Advanced To-Do List

Welcome to the **Advanced To-Do List** application! This Python application allows you to manage your tasks in a simple and intuitive way. Built with **Tkinter**, the app provides a graphical user interface to add, edit, delete, and mark tasks as completed. Additionally, your tasks are saved in a JSON file so they persist between sessions.

## Features
- **Add Tasks**: Add new tasks to your to-do list.
- **Delete Tasks**: Remove tasks from the list.
- **Edit Tasks**: Modify the description of existing tasks.
- **Mark Tasks as Completed**: Mark tasks as completed with a checkmark.
- **Clear All Tasks**: Clear all tasks from the list.
- **Persistent Storage**: Tasks are saved in a `tasks.json` file and are loaded automatically when the application starts.

## Requirements
- **Python**: The application is built using Python 3.
- **Tkinter**: The graphical user interface (GUI) is built using the Tkinter library, which is included with most Python installations.
- **JSON**: The tasks are stored in a JSON file for persistence between sessions.

## Installation

1. Make sure you have Python 3 installed. You can download Python from [python.org](https://www.python.org/downloads/).
2. Tkinter is included by default in Python installations, so no separate installation is required.

## How to Run the Application

1. Download or clone the repository to your local machine.
2. Navigate to the folder containing the script.
3. Run the following command to start the application:

    ```bash
    python todo_list.py
    ```

   This will launch the To-Do List application window.

## How to Use

- **Add Task**: Enter the task in the input field and click the "Add" button to add it to the list.
- **Delete Task**: Select a task from the list and click the "Delete" button to remove it.
- **Edit Task**: Select a task and click the "Edit" button to update its description.
- **Mark as Completed**: Select a task and click the "Complete" button to mark it as completed with a checkmark.
- **Clear All Tasks**: Click the "Clear All" button to delete all tasks from the list.
- The application saves your tasks in a `tasks.json` file, which loads automatically each time you open the app.

## Code Overview

- **Task Management**:
    - Add, delete, edit, and mark tasks as completed.
    - Tasks are saved in a local JSON file (`tasks.json`).

- **User Interface**:
    - Simple interface with buttons for each action (Add, Delete, Edit, Complete, Clear All).
    - A listbox is used to display tasks.
    - Input field for adding new tasks.

- **Persistence**:
    - Tasks are saved in a JSON file (`tasks.json`) and loaded on startup, so the app remembers your tasks between sessions.

## Credits

This project was developed by Mr. Tapendra chy from Quantum University. Feel free to fork the repository and contribute!

**Thank You** ✔️
