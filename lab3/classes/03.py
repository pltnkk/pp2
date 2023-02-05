a = int(input())
b = int(input())

class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    def area(self):
        return self.lenght * self.width

rec = Rectangle(a,b)

print("Area of rectangle:", rec.area())