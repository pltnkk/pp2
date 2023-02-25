import re

str = input()
def spaces(str):

    a =  re.sub(r"(\w)([A-Z])", r"\1 \2", str)
    return a
print(spaces(str))