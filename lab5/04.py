import re

a = map(str, input().split())

u = re.findall( "[A-Z][a-z]+", a )

print(u)