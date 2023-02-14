
n = int(input())
def ev():

    for even in range(0, n+1, 2):
        yield even

lst = []
for i in ev():
    lst.append(str(i))

print(", ".join(lst))