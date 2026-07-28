"""
number = int (input("Enter a number: "))

if number % 2 == 0:
    print ("Even")
else: 
    print ("Odd")
"""

"""
if number % 2 !=0:
   print ("Even")
else:
    print ("Odd")
"""
"""
# print even numbers from 1- 100
print("-----------------")
print("Even Numbers")
for even in range (2, 101, 2):
    print(even)

# print odd numbers from 1- 100
print("-----------------")
print ("Odd Numbers")
for odd in range (1, 101, 2):
   print(odd)
"""

def print_even_numbers(stop):
    for d in range (2, stop + 1, 2):
        print (d)

number_to_print = int ( input("Enter a range: "))

print_even_numbers(number_to_print)


def print_odd_numbers(stop):
    for d in range (1, stop + 1, 2):
        print (d)

number_to_print = int ( input("Enter a range: "))

print_odd_numbers(number_to_print)