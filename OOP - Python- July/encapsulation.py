class Encapsulatedcar:
    def __init__(self, color, brand, model):
        self.__color = "color"
        self.__brand = "brand"
        self.__model = "model"

def get_color(self):
    return self.__colour

def get_brand (self):
    return self.__brand

def update_brand(self, value):
    self.__brand = value

def update_brand(self, value):
    self.__brand = value

def get_details(self):
    print("Here are the details of the car")
    print(f"color: {self.__color}")
    print(f"brand: {self.__brand}")
    print(f"Model: {self.__model}")

encap = Encapsulatedcar("Red", "Canry", "bes1222")
encap.update_brand("Benz")
print(encap.get_color())
print (encap.get_brand())

color= input("Tell the color of the car: ")
brand= input("Tell the brand of the car: ")
model= input("Tell the model of the car: ")

my_car = Car ( color, brand, model)
my_car.get_details()


