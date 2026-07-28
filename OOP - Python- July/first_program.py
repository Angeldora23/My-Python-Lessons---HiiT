class student:
    matric_number = "20304050"
    first_name = "Dorathy"
    last_name = "Etim"

student_1 = student()
student_1.matric_number = "changed matric number"
student_1.first_name = "Dorathy"
student_1.last_name = "Etim"

print(student_1.matric_number)
print(f"student_1.first_name = Dorathy")
print(f"student_1.last_name = Etim")
