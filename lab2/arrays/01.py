cars = ["Ford", "Volvo", "BMW"]
print(cars)
#2
print(cars[0])
#3
cars[0]= "Toyota"
print(cars)
#4
x = len(cars)
print(x)
#5
for i in cars:
    print(i)
#6
cars.append("Honda")
print(cars)
#7
cars.pop(1)
print(cars)
#8
cars.remove("Volvo")
print(cars)#The list's remove() method only removes the first occurrence of the specified value.


