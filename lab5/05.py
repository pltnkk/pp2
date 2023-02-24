import re

a = input()

b = re.findall("a.+b$", a)

print(b)