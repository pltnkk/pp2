import math


a, b = int(input()), int(input())

c, d = int(input()), int(input())

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def show(self):
        print("Point({}, {})".format(self.x, self.y))
    def move(self, x, y):
        self.x += x
        self.y += y

    def distt(self, x1, y1):
        return math.sqrt((self.x - x1) ** 2 + (self.y - y1) ** 2)

cl = Point(a,b)

cl.show()



print("Distance between the two points", cl.distt(c,d))