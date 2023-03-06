

a = input()
cntup = 0
cntlo = 0
for i in a:
    if i.isupper():
        cntup += 1
    elif i.islower():
        cntlo += 1

print("Upper casse letter: ", cntup)
print("Lower case letter: ", cntlo)