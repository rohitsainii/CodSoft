import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if task_string:
        tasks.append(task_string)
        task_listbox.insert(tk.END, task_string)
        task_field.delete(0, tk.END)
        save_task_to_db(task_string)
    else:
        messagebox.showinfo('Error', 'Field is Empty.')

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = int(selected_task_index[0])
        task_to_delete = tasks.pop(index)
        task_listbox.delete(selected_task_index)
        delete_task_from_db(task_to_delete)
    else:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    confirmed = messagebox.askyesno('Delete All', 'Are you sure you want to delete all tasks?')
    if confirmed:
        tasks.clear()
        task_listbox.delete(0, tk.END)
        delete_all_tasks_from_db()

def save_task_to_db(task):
    cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task,))
    db_connection.commit()

def delete_task_from_db(task):
    cursor.execute('DELETE FROM tasks WHERE title = ?', (task,))
    db_connection.commit()

def delete_all_tasks_from_db():
    cursor.execute('DELETE FROM tasks')
    db_connection.commit()

def load_tasks_from_db():
    cursor.execute('SELECT title FROM tasks')
    for row in cursor.fetchall():
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("500x450")
    guiWindow.resizable(0, 0)

    db_connection = sql.connect('listOfTasks.db')
    cursor = db_connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')

    tasks = []

    header_frame = tk.Frame(guiWindow)
    functions_frame = tk.Frame(guiWindow)
    listbox_frame = tk.Frame(guiWindow)

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = ttk.Label(
        header_frame,
        text="To-Do List",
        font=("Arial", 24)
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Arial", 12, "bold")
    )
    task_label.place(x=30, y=40)

    task_field = ttk.Entry(
        functions_frame,
        font=("Arial", 12),
        width=18
    )
    task_field.place(x=30, y=80)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=24,
        command=add_task
    )
    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        command=delete_task
    )
    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=24,
        command=delete_all_tasks
    )
    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=24,
        command=guiWindow.quit
    )
    add_button.place(x=30, y=120)
    del_button.place(x=30, y=160)
    del_all_button.place(x=30, y=200)
    exit_button.place(x=30, y=240)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=26,
        height=13,
        selectmode='SINGLE'
    )
    task_listbox.place(x=10, y=20)

    load_tasks_from_db()
    for task in tasks:
        task_listbox.insert(tk.END, task)

    guiWindow.mainloop()
    db_connection.close()
