from math import sqrt

n = int(input())
lst = []
for i in range(0,n):
    a = int(input())
    lst.append(a)

isprime = lambda x : all( x % i != 0 for i in range(2, int(sqrt(x)) + 1))

numbers = list(filter(isprime,lst))

print(numbers)