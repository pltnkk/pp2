lst = map(int, input().split())
def histogram(x):
    for i in x:
        print( "*" * i)

histogram(lst)
