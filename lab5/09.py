import re

s = input()
def space(s):
    b = re.sub(r"(\w)([A-Z])", "\1 \2", s)

    return b
space(s)





