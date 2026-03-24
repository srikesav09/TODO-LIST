# 📝 To-Do List Application (Python + MySQL + Tkinter)

## 📌 Overview

This is a simple **To-Do List desktop application** built using:

* **Python (Tkinter)** for GUI
* **MySQL** for database storage

It allows users to **add, update, delete, and view tasks** with date and time.

---

## 🚀 Features

* ✅ Add new tasks with date & time
* 🔄 Update existing tasks
* ❌ Delete tasks
* 📋 Display tasks in a table (Treeview)
* 💾 Stores tasks in MySQL database
* 🗂️ Saves tasks & deleted logs in text files

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* MySQL
* mysql-connector-python

---

## ⚙️ Setup Instructions

### 1️⃣ Install Required Libraries

```bash
pip install mysql-connector-python pandas
```

---

### 2️⃣ Setup MySQL Database

Run the following SQL commands:

```sql
CREATE DATABASE todo;

USE todo;

CREATE TABLE tasks (
    s_no INT AUTO_INCREMENT PRIMARY KEY,
    date VARCHAR(20),
    Time VARCHAR(20),
    tasks VARCHAR(255)
);
```

---

### 3️⃣ Update Database Credentials

In your Python file, update:

```python
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='todo'
)
```

---

### 4️⃣ Run the Application

```bash
python your_file_name.py
```

---

## 📂 Project Structure

```
📁 project-folder
│── main.py
│── todo tasks.txt
│── todo deleted.txt
```

---

## 🖥️ How It Works

1. Enter **Date, Time, and Task**
2. Click:

   * ➕ Insert → Add new task
   * 🔄 Update → Modify selected task
   * ❌ Delete → Remove selected task
3. Tasks are displayed in the table below

---

## ⚠️ Common Issues & Fixes

### ❌ MySQL Connection Error

* Ensure MySQL server is running
* Check username/password
* Verify port (default: 3306)

### ❌ Module Not Found

```bash
pip install mysql-connector-python
```

---

## 🔮 Future Improvements

* 📅 Date picker instead of manual input
* ⏰ Notifications/reminders
* 🔍 Search & filter tasks
* 🌐 Web version (using Node.js / React)
* 🔐 User login system

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Author

Developed by **Srikesav M**

---
