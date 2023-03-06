import os

path = "/Users/kpiltann/Desktop/pp2/lab6/directoy/08.py"

if os.path.exists(path):
    os.remove(path)
else:
    print("The file doesn't exist")

