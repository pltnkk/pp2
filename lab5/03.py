import re

x = map(str, input().split())

def findd(x):
    z = re.findall("[a-z]+_[a-z]+", x)
    for i in z:
        print(i)

findd(x)
