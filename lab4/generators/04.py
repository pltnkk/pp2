a, b = int(input()), int(input())

def squares():
    for i in range(a,b+1):
        yield i ** 2

sqr = []
for num in squares():
    sqr.append(str(num))

print(", ".join(sqr))