a = int(input())

def div():
    i = 0
    while i <= a:
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i+=1

divisible = []
for i in div():
    divisible.append(str(i))

print(", ".join(divisible))
