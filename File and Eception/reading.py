file_name = "files/names.txt"
with open (file_name, "r") as file:
    content = file.readlines()

print(content) #return a list
