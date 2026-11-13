# 🎓 Python Student Management System

A beginner-friendly **Student Management System** built using Python and SQLite. This project helps manage student records through a simple command-line interface.

## ✨ Features

- Add new student records
- View all student records
- Search students by ID or name
- Update student information
- Delete student records with confirmation
- Store student details using SQLite database
- Validate required fields and positive ages
- Prevent duplicate student IDs and email addresses

## 🛠️ Technologies Used

- **Python 3.8+**
- **SQLite**
- Python's built-in `sqlite3` module

No additional packages are required.

## 🚀 How to Run the Project

### Step 1: Download the Project

Clone this repository:

```bash
git clone https://github.com/narmi235/Python-Student-Management-System.git
```

### Step 2: Open the Project Folder

```bash
cd Python-Student-Management-System
```

### Step 3: Run the Python File

```bash
python student_management.py
```

If needed, use:

```bash
python3 student_management.py
```

## 📋 Application Menu

The program provides the following options:

```text
========== STUDENT MANAGEMENT SYSTEM ==========
1. Add student
2. View all students
3. Search student
4. Update student
5. Delete student
0. Exit
================================================
```

Select an option and follow the instructions displayed on the screen.

## 📁 Project Structure

```text
Python-Student-Management-System/
│
├── student_management.py
├── README.md
└── .gitignore
```

## 🗄️ Database

- Student records are stored in an SQLite database named `students.db`.
- The database is created automatically when the program runs for the first time.
- Student ID and email must be unique.
- The database is stored locally on your computer.

## 🎯 Future Improvements

- Add a graphical user interface (GUI)
- Export student records to Excel or CSV
- Add student login functionality
- Add sorting and filtering options

## 👨‍💻 Project Purpose

This project is developed for learning and demonstrating Python programming, database connectivity, and basic CRUD operations.

---

⭐ If you find this project useful, please consider giving it a star!
