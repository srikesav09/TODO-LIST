import mysql.connector
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# MySQL Connection
con = mysql.connector.connect(host='localhost', user='root', password='srikesav9@', database='todo')

# Insert Function
def insert():
    date = date_entry.get()
    time = time_entry.get()
    task = task_entry.get()
    if not (date and time and task):
        messagebox.showerror("Input Error", "All fields are required!")
        return
    cu = con.cursor()
    cu.execute("INSERT INTO tasks(date, Time, tasks) VALUES(%s, %s, %s)", (date, time, task))
    con.commit()
    with open("todo tasks.txt", 'a') as f:
        f.write(f"{task}\n")
    messagebox.showinfo("Success", "Task Inserted Successfully!")
    refresh_tasks()

# Update Function
def update():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Selection Error", "Select a task to update.")
        return
    no = tree.item(selected)['values'][0]
    date = date_entry.get()
    time = time_entry.get()
    task = task_entry.get()
    cu = con.cursor()
    cu.execute("UPDATE tasks SET date=%s, Time=%s, tasks=%s WHERE s_no=%s", (date, time, task, no))
    con.commit()
    messagebox.showinfo("Success", "Task Updated Successfully!")
    refresh_tasks()

# Delete Function
def delete():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Selection Error", "Select a task to delete.")
        return
    no = str(tree.item(selected)['values'][0])
    cu = con.cursor()
    cu.execute("DELETE FROM tasks WHERE s_no=%s", [no])
    con.commit()
    with open("todo deleted.txt", 'a') as f:
        f.write(no + '\n')
    messagebox.showinfo("Success", "Task Deleted Successfully!")
    refresh_tasks()

# Display/Refresh Function
def refresh_tasks():
    for item in tree.get_children():
        tree.delete(item)
    cu = con.cursor()
    cu.execute("SELECT * FROM tasks")
    rows = cu.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)

# On Treeview Item Select
def on_select(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected)['values']
        date_entry.delete(0, tk.END)
        date_entry.insert(0, values[1])
        time_entry.delete(0, tk.END)
        time_entry.insert(0, values[2])
        task_entry.delete(0, tk.END)
        task_entry.insert(0, values[3])

# GUI Window
root = tk.Tk()
root.title("To-Do List with MySQL")
root.geometry("700x500")

# Labels and Entry Fields
tk.Label(root, text="Date (dd/mm/yyyy):").place(x=20, y=20)
date_entry = tk.Entry(root, width=30)
date_entry.place(x=160, y=20)

tk.Label(root, text="Time (hh:mm):").place(x=20, y=60)
time_entry = tk.Entry(root, width=30)
time_entry.place(x=160, y=60)

tk.Label(root, text="Task:").place(x=20, y=100)
task_entry = tk.Entry(root, width=30)
task_entry.place(x=160, y=100)

# Buttons
tk.Button(root, text="Insert Task", width=15, command=insert).place(x=450, y=20)
tk.Button(root, text="Update Task", width=15, command=update).place(x=450, y=60)
tk.Button(root, text="Delete Task", width=15, command=delete).place(x=450, y=100)

# Treeview to Display Tasks
tree = ttk.Treeview(root, columns=('s_no', 'date', 'time', 'task'), show='headings')
tree.heading('s_no', text='S.No')
tree.heading('date', text='Date')
tree.heading('time', text='Time')
tree.heading('task', text='Task')
tree.place(x=20, y=160, width=650, height=300)
tree.bind("<ButtonRelease-1>", on_select)

# Initial load
refresh_tasks()

root.mainloop()
