# Python Student Management System

A beginner-friendly command-line application for managing student records with Python and SQLite.

## Features

- Add new students
- View all student records
- Search by student ID or name
- Update student information
- Delete student records with confirmation
- Stores records locally in an SQLite database (`students.db`)
- Validates required fields and positive ages

## Requirements

- Python 3.8 or newer
- No third-party packages required (uses Python's built-in `sqlite3` module)

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python student_management.py
   ```

   On some systems, use `python3 student_management.py`.

4. Choose an option from the menu and follow the prompts.

The `students.db` database file is created automatically the first time the program runs.

## Project structure

```text
Python-Student-Management-System/
├── student_management.py
├── README.md
└── .gitignore
```

## Notes

- Student ID and email must be unique.
- The database is stored in the same folder as the Python script.
- This is a local learning project, not a production student information system.
