
a = int(input())

class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, lenght):

        self.lenght = lenght
    def area(self):
        return self.lenght * self.lenght

sq = Square(a)
sh = Shape()
print( "Area of square:", sq.area())
print( "Area of shape:", sh.area())





