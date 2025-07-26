import tkinter as tk
from tkinter import messagebox, filedialog
import json

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def edit_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task)

        def save_edited_task():
            new_task = edit_entry.get()  # Get the updated task from the edit_entry widget
            if new_task:
                task_listbox.delete(selected_task_index)
                task_listbox.insert(selected_task_index, new_task)
                task_entry.delete(0, tk.END)
                save_tasks()
                edit_window.destroy()
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")

        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Task")
        edit_window.geometry("300x150")
        tk.Label(edit_window, text="Edit your task:", font=("Arial", 12)).pack(pady=10)
        edit_entry = tk.Entry(edit_window, font=("Arial", 12), width=30)
        edit_entry.pack(pady=5)
        edit_entry.insert(0, task)  # Insert the selected task into the edit entry field

        save_button = tk.Button(edit_window, text="Save", font=("Arial", 12), bg="#4CAF50", fg="white", command=save_edited_task)
        save_button.pack(pady=10)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit!")

def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"✔ {task}")
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

def clear_tasks():
    task_listbox.delete(0, tk.END)
    save_tasks()

# Create main window
root = tk.Tk()
root.title("Advanced To-Do List")
root.geometry("500x600")
root.configure(bg="#f4f4f4")

# Title Label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 24, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

# Input field
task_entry = tk.Entry(root, font=("Arial", 14), width=40, bd=2, relief=tk.GROOVE)
task_entry.pack(pady=10, padx=20)

# Buttons
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack()

add_button = tk.Button(button_frame, text="Add", font=("Arial", 12), bg="#4CAF50", fg="white", width=12, command=add_task)
add_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete", font=("Arial", 12), bg="#FF5733", fg="white", width=12, command=delete_task)
delete_button.grid(row=0, column=1, padx=5, pady=5)

edit_button = tk.Button(button_frame, text="Edit", font=("Arial", 12), bg="#FFC300", fg="black", width=12, command=edit_task)
edit_button.grid(row=0, column=2, padx=5, pady=5)

complete_button = tk.Button(button_frame, text="Complete", font=("Arial", 12), bg="#008CBA", fg="white", width=12, command=mark_completed)
complete_button.grid(row=1, column=0, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear All", font=("Arial", 12), bg="#A9A9A9", fg="white", width=12, command=clear_tasks)
clear_button.grid(row=1, column=1, padx=5, pady=5)

# Task List
task_listbox = tk.Listbox(root, font=("Arial", 14), selectmode=tk.SINGLE, height=15, bd=2, relief=tk.SOLID)
task_listbox.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)

# Load tasks on startup
load_tasks()

# Run the application
root.mainloop()
