class Triangle:
    # this is not necessary for init
    a = 2
    y = 4
    z = 5

    def __init__(self, side1, side2, side3):
        self.a = side1
        self.b = side2
        self.c = side3

    def perimeter(self):
        per = self.a + self.b + self.c
        print(f"The perimeter is: {per}")
        return per



t1 = Triangle (10, 12,15)
t2 =Triangle (11, 13,16)

value = t2.perimeter()
print(value)


