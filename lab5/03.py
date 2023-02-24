import re

x = map(str, input().split())

def findd(x):
    z = re.findall("[a-z][_][a-z", x)
    if z:
        return True
    else:
        return False

print(findd(x))
