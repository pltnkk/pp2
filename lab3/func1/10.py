def unique(listt):
    ue = []
    for el in listt:
        if el not in ue:
            ue.append(el)

    return ue

n =int(input())
lst = []
for i in range(0,n):
    a = input()
    lst.append(a)

print(unique(lst))