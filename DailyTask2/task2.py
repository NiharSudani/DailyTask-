import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
""")
conn.commit()


def InsertData():
    print("<<<Insert Data>>>")
    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()

    if first_name and last_name and age.isdigit() and course:
        cursor.execute(
            "INSERT INTO students (first_name, last_name, age, course) VALUES (?, ?, ?, ?)",
            (first_name, last_name, int(age), course),
        )
        conn.commit()
        print("Student added successfully!")
    else:
        print("Error: Please provide valid input for all fields.")


def ListStudents():
    print("<<<List Student Data>>>")
    cursor.execute("SELECT id, first_name, last_name, age, course FROM students")
    students = cursor.fetchall()

    if students:
        print("\nStudent List:")
        print("-" * 50)
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]} {student[2]}, Age: {student[3]}, Course: {student[4]}")
        print("-" * 50)
    else:
        print("\nNo students found.")


def UpdateData():
    print("<<<Update Data>>>")
    ListStudents()
    student_id = input("Enter the ID of the student to update: ").strip()

    if student_id.isdigit():
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()
        if student:
            first_name = input("Enter New First Name: ").strip() or student[1]
            last_name = input("Enter New Last Name: ").strip() or student[2]
            age = input("Enter New Age: ").strip() or str(student[3])
            course = input("Enter New Course: ").strip() or student[4]

            if age.isdigit():
                cursor.execute(
                    """
                    UPDATE students 
                    SET first_name = ?, last_name = ?, age = ?, course = ? 
                    WHERE id = ?
                    """,
                    (first_name, last_name, int(age), course, student_id),
                )
                conn.commit()
                print("Student updated successfully!")
            else:
                print("Error: Age must be a valid number.")
        else:
            print("Error: Student not found.")
    else:
        print("Error: Invalid ID.")


def DeleteData():
    print("<<<Delete Data>>>")
    ListStudents()
    student_id = input("Enter the ID of the student to delete: ").strip()

    if student_id.isdigit():
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        if cursor.rowcount:
            print("Student deleted successfully!")
        else:
            print("Error: Student not found.")
    else:
        print("Error: Invalid ID.")


while True:
    print("\n Student Management System")
    print("1. Insert Student")
    print("2. List Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        InsertData()
    elif choice == "2":
        ListStudents()
    elif choice == "3":
        UpdateData()
    elif choice == "4":
        DeleteData()
    elif choice == "5":
        print("<<<Goodbye>>>")
        break
    else:
        print("Error: Invalid choice. Please try again.")

conn.close()
