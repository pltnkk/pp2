import re

s = input()

b = print(re.findall(r"(\w)([A-Z])", s))

print(" ".join(b))






