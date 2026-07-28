every_body_in_class = ["Neymar" , "Ronaldo" , "Halland" , "Mbappe"]
#getting first and last person on the list using the index
first_person = every_body_in_class [0]

last_person = every_body_in_class [-1]
print(last_person)
numbers = [3,5,7,1,4,6,8,9,10,2]
numbers.sort()
# print (names)

# sorting of names
names = ["Tinubu" , "Zaria", "Yakubu", "Dorcas", "Mohammed", "Abubakar", "Balewa", "balewa"]
names.sort()
# print (names)


# adding to the list
names.append ("Pelumi")
names.append ("Dorathy")

#checking the length
length_of_the_names = len(names)
print(f"we now have (length_of_names) in the list")
# print (names)

# remove from the list 
names.remove("balewa")
# print  (names)

cars = ["Toyota", "Korope", "Mercedes", "Lexus"]
cars.insert (1 , "Tesla")
# print(cars)
cars.pop(2)
# print(cars)

names = ["Tinubi" , "Zaria", "Yakubu", "Mohammed"]
print(names)
names[0] = "Tinubu"
print(names)

#merge list into one
every_body_in_class.extend(cars)
print(every_body_in_class)
