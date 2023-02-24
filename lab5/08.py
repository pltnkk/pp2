import re

s = input()

t = re.sub("(\w)[A-Z]", "\1 \2", s)

print(t)