N = int(input())
def sqr():
    for i in range(N):
        yield i ** 2

for i in sqr():
    print( i, end= " ")

