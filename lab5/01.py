import re

a = input()

regx = "^a(b)*$"
if re.search(regx, a):
    print('True')
else:
    print("False")



