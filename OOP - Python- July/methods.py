
class car:
    def __init__(self, color, brand, model):
        self.color = "color"
        self.brand = "brand"
        self.model = "model"
        self.is_running = False
        self.programmer = "Favour"

def start (self):
    self.is_running = True
    print("The car is starting.....")

def stop (self):
    self.is_running = False
    print ("The car is stopping....")

my_car = car ("Black", "Tesla", "I don't know my fans")

"""
print(f"Color: {my_car.color}")
print(f"Brand: {my_car.brand}")
print(f"Model: {my_car.model}")
print(f"Is running: {my_car.is_running}")

my_car.start()
print(f"is runninh: {my_car.is_running}")
my_car.stop()
"""
#inheritance
class Train (car):
    pass

ti = Train("blue", "Banko", "TT44")

print(f"Color: {my_car.color}")
print(f"Brand: {my_car.brand}")
print(f"Model: {my_car.model}")
print(f"Is running: {my_car.is_running}")

