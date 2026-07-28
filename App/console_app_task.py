"""
Task: Developing a Console Application 
-Write a Python Program that collects student information  
like, 
Matric number: 
Email: 
Department: 
Age: 
Faculty etc.

Stores the information using SQLite database. 
- The user of the application should be able decide  
whether they want to create new student record,  
retrieve existing student record, update a certain  
record or delete it (CRUD). 
- Additional note (still thinking about it): Might add  
that they should be able export the info into a txt file  
and it should contain all student info.
"""

import sqlite3

print("welcome to student records")

while True:
    print("select an option: ")
    print("1- Add New record")
    print("2- Retrieve student record")
    print("3- Update student record")
    print("4- Delete student record")
    print("5- Export record as txt")
    print("6- Exit")

    option_input = input("Enter your option: ")

    if not option_input.isdigit():
        print("Please enter a number from 1 to 6.")
        continue

    option = int(option_input)

    if option == 1:
        matric_number = input("Enter your matric number: ")
        email = input("Enter your email: ")
        department = input("Enter your department: ")
        age = input("Enter your age: ")
        faculty = input("Enter your faculty: ")
        level = input("Enter your level: ")

        with sqlite3.connect("student_records.db") as conn:
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS 
            students (
                id INTEGER PRIMARY KEY,
                matric_number TEXT UNIQUE,
                email TEXT,
                department TEXT,
                age INTEGER,
                faculty TEXT,
                level TEXT
            )
            """)

            sql = """INSERT INTO students (matric_number, email, department, age, faculty, level) 
            VALUES (?, ?, ?, ?, ?, ?)"""

            try:
                cursor.execute(sql, (matric_number, email, department, age, faculty, level))
                conn.commit()
                print("Student added successfully.")
            except sqlite3.IntegrityError:
                print(f"A student with matric number '{matric_number}' already exists.")

    elif option == 2:
        with sqlite3.connect("student_records.db") as conn:
            cursor = conn.cursor()

            sql = """SELECT * FROM students"""

            cursor.execute(sql)
            record = cursor.fetchall()

            if len(record) == 0:
                print("No students found.")

            for row in record:
                student_id = row[0]
                matric_number = row[1]
                email = row[2]
                department = row[3]
                age = row[4]
                faculty = row[5]
                level = row[6]

                print(f"""
                Student ID: {student_id}
                Matric Number: {matric_number}
                Email: {email}
                Department: {department}
                Age: {age}
                Faculty: {faculty}
                Level: {level}
                """)

    elif option == 3:
        with sqlite3.connect("student_records.db") as conn:
            cursor = conn.cursor()

            student_id = input("Enter the student ID to update: ")
            new_email = input("Enter the new email: ")

            sql = """UPDATE students SET email = ? WHERE id = ?"""
            cursor.execute(sql, (new_email, student_id))
            conn.commit()

            if cursor.rowcount == 0:
                print(f"No student found with ID '{student_id}'.")
            else:
                print("Student record updated successfully.")

    elif option == 4:
        with sqlite3.connect("student_records.db") as conn:
            cursor = conn.cursor()

            student_id = input("Enter the student ID to delete: ")

            sql = """DELETE FROM students WHERE id = ?"""
            cursor.execute(sql, (student_id,))
            conn.commit()

            if cursor.rowcount == 0:
                print(f"No student found with ID '{student_id}'.")
            else:
                print("Student record deleted successfully.")

    elif option == 5:
        with sqlite3.connect("student_records.db") as conn:
            cursor = conn.cursor()

            sql = """SELECT * FROM students"""
            cursor.execute(sql)
            record = cursor.fetchall()

            if len(record) == 0:
                print("No students to export.")
                continue

            file = open("students_export.txt", "w")

            for row in record:
                student_id = row[0]
                matric_number = row[1]
                email = row[2]
                department = row[3]
                age = row[4]
                faculty = row[5]
                level = row[6]

                file.write(f"Student ID: {student_id}\n")
                file.write(f"Matric Number: {matric_number}\n")
                file.write(f"Email: {email}\n")
                file.write(f"Department: {department}\n")
                file.write(f"Age: {age}\n")
                file.write(f"Faculty: {faculty}\n")
                file.write(f"Level: {level}\n")
                file.write("------------------------\n")

            file.close()
            print("Records exported to students_export.txt")

    elif option == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid option, please choose a number from 1 to 6.")