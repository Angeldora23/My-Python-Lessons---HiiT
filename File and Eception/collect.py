first_name = input("Enter the my name: ")
last_name = input ("Enter the last name: ")
age = input ("Enter your age: ")

file_name = "files/person.txt"
with open (file_name, "w") as file:
    file.write(f"First_name: {first_name}\n")
    file.write(f"Last_name: {last_name}\n")
    file.write(f"Age: {age}\n")
    