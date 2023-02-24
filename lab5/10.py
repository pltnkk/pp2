import re


a = input()

def snaaake(a):
    string = re.sub("(?<!^)(?=[A-Z])", "_", a).lower()
    return string

print(snaaake(a))

