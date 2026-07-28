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


from ast import Import


import sqlite3

print ("welcome to student records")

print ("select an option: ")
print ("1- Add New record")
print ("2- Retrieve student record")
print ("3- Update student record")
print ("4- Delete student record")  
print ("5- Export record as txt")
print ("6- Exit")

option = int(input ("Enter your option: "))

if option == 1:
    matric_number = input ("Enter your matric number: ")
    email = input ("Enter your email: ")
    department = input ("Enter your department: ")
    age = input ("Enter your age: ")
    faculty = input ("Enter your faculty: ")
    level = input ("Enter your level: ")


    with sqlite3.connect ("student_records.db") as conn:
        cursor = conn.cursor()

        cursor.execute ("""
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
        cursor.execute(sql, (matric_number, email, department, age, faculty, level))

elif option == 2:
    with sqlite3.connect ("student_records.db") as conn:
        cursor = conn.cursor()

        sql = """SELECT * FROM students"""

        cursor.execute (sql)
        record = cursor.fetchall()

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
    with sqlite3.connect ("student_records.db") as conn:
        cursor = conn.cursor()

        student_id = input ("Enter the student ID to update: ")
        new_email = input ("Enter the new email: ")

        sql = """UPDATE students SET email = ? WHERE id = ?"""
        cursor.execute (sql, (new_email, student_id))
        conn.commit()
        print ("Student record updated successfully.")



