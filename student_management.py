"""
Python Student Management System
A simple command-line student record manager using SQLite.

Run:
    python student_management.py
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("students.db")


def connect():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL CHECK(age > 0),
                course TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL
            )
        """)


def prompt_nonempty(label):
    while True:
        value = input(label).strip()
        if value:
            return value
        print("This field cannot be empty.")


def prompt_age():
    while True:
        raw = input("Age: ").strip()
        try:
            age = int(raw)
            if age > 0:
                return age
        except ValueError:
            pass
        print("Please enter a valid age (a positive whole number).")


def add_student():
    print("\n--- Add Student ---")
    student_id = prompt_nonempty("Student ID: ")
    name = prompt_nonempty("Full name: ")
    age = prompt_age()
    course = prompt_nonempty("Course: ")
    email = prompt_nonempty("Email: ")
    phone = prompt_nonempty("Phone: ")

    try:
        with connect() as conn:
            conn.execute(
                """INSERT INTO students
                   (student_id, name, age, course, email, phone)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (student_id, name, age, course, email, phone),
            )
        print("Student added successfully.")
    except sqlite3.IntegrityError as error:
        print(f"Could not add student: {error}. Check that the ID and email are unique.")


def list_students():
    print("\n--- All Students ---")
    with connect() as conn:
        rows = conn.execute(
            """SELECT student_id, name, age, course, email, phone
               FROM students ORDER BY name COLLATE NOCASE"""
        ).fetchall()

    if not rows:
        print("No student records found.")
        return

    print("-" * 105)
    print(f"{'ID':<12} {'NAME':<22} {'AGE':<5} {'COURSE':<18} {'EMAIL':<28} {'PHONE':<15}")
    print("-" * 105)
    for row in rows:
        student_id, name, age, course, email, phone = row
        print(f"{student_id:<12} {name[:21]:<22} {age:<5} {course[:17]:<18} {email[:27]:<28} {phone[:14]:<15}")
    print("-" * 105)
    print(f"Total students: {len(rows)}")


def search_student():
    print("\n--- Search Student ---")
    term = prompt_nonempty("Enter student ID or name: ")
    with connect() as conn:
        rows = conn.execute(
            """SELECT student_id, name, age, course, email, phone
               FROM students
               WHERE student_id LIKE ? OR name LIKE ?
               ORDER BY name COLLATE NOCASE""",
            (f"%{term}%", f"%{term}%"),
        ).fetchall()

    if not rows:
        print("No matching students found.")
        return

    for row in rows:
        print_student_details(row)


def print_student_details(row):
    labels = ("Student ID", "Name", "Age", "Course", "Email", "Phone")
    print("\n" + "-" * 32)
    for label, value in zip(labels, row):
        print(f"{label}: {value}")
    print("-" * 32)


def update_student():
    print("\n--- Update Student ---")
    student_id = prompt_nonempty("Enter the ID of the student to update: ")

    with connect() as conn:
        row = conn.execute(
            "SELECT student_id, name, age, course, email, phone FROM students WHERE student_id = ?",
            (student_id,),
        ).fetchone()

    if not row:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")
    name = input(f"Name [{row[1]}]: ").strip() or row[1]
    age_text = input(f"Age [{row[2]}]: ").strip()
    if age_text:
        try:
            age = int(age_text)
            if age <= 0:
                raise ValueError
        except ValueError:
            print("Invalid age. Update cancelled.")
            return
    else:
        age = row[2]
    course = input(f"Course [{row[3]}]: ").strip() or row[3]
    email = input(f"Email [{row[4]}]: ").strip() or row[4]
    phone = input(f"Phone [{row[5]}]: ").strip() or row[5]

    try:
        with connect() as conn:
            conn.execute(
                """UPDATE students
                   SET name = ?, age = ?, course = ?, email = ?, phone = ?
                   WHERE student_id = ?""",
                (name, age, course, email, phone, student_id),
            )
        print("Student updated successfully.")
    except sqlite3.IntegrityError as error:
        print(f"Could not update student: {error}")


def delete_student():
    print("\n--- Delete Student ---")
    student_id = prompt_nonempty("Enter the ID of the student to delete: ")

    with connect() as conn:
        row = conn.execute(
            "SELECT name FROM students WHERE student_id = ?", (student_id,)
        ).fetchone()

    if not row:
        print("Student not found.")
        return

    confirm = input(f"Delete {row[0]} ({student_id})? (y/n): ").strip().lower()
    if confirm == "y":
        with connect() as conn:
            conn.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        print("Student deleted successfully.")
    else:
        print("Delete cancelled.")


def show_menu():
    print("""
========== STUDENT MANAGEMENT SYSTEM ==========
1. Add student
2. View all students
3. Search student
4. Update student
5. Delete student
0. Exit
================================================
""")


def main():
    initialize_database()
    print("Welcome to the Student Management System!")

    actions = {
        "1": add_student,
        "2": list_students,
        "3": search_student,
        "4": update_student,
        "5": delete_student,
    }

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Thank you for using the Student Management System. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please select 0, 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
