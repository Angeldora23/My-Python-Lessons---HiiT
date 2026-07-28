file_name = "files/names.txt"
with open (file_name, "r") as file:
    for text in file:
        print(text.strip())
