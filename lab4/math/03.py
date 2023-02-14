from math import tan, pi


a = float(input("Input number of sides: "))
b = float(input(("Input the length of a side: ")))


area = a * (b*b) / (4 * tan(pi/a))


print("The area of the polygon is: ", area)