import os

path = "/Users/kpiltann/Desktop/pp2/lab6"

f = open(path)

def exi(path):
    if os.access(path, os.F_OK):
        print(f"{path} exists")
    else:
        print(f"{path} doesn't exist")

def readfile(path):
    if os.access(path, os.R_OK):
        print(f"{path} is readable")
    else:
        print(f"{path} isn't readable")

def writefile(path):
    if os.access(path, os.W_OK):
        print(f"{path} is writable")
    else:
        print(f"{path} isn't writable")
def exe(path):
    if os.access(path, os.X_OK):
        print(f"{path} is executable")
    else:
        print(f"{path} isn't executable")