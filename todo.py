import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            tasks = f.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())

def save_tasks():
    with open(FILE_NAME, "w") as f:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Ошибка", "Введите задачу!")

def remove_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу для удаления!")

# GUI
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

add_button = tk.Button(root, text="Добавить", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Удалить", command=remove_task)
remove_button.pack()

load_tasks()
root.mainloop()
