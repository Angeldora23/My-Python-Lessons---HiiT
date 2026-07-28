condition = True

while condition:
    y = int (input("Enter a number"))
    z = int (input("Enter another number"))

    add = y + z
    print(f"{y} + {z} = {add}")

    print("----------------------------------------")
    print("do you still want to calculate")
    print("----------------------------------------")

    response = input ("To continue enter 'yes': ")

    if response.lower() == "yes":
        condition = True 
    else: 
        condition = False

