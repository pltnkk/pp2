import os

def copyfile(file1, file2):
    a = open(file1, "r")
    b = a.read()
    a.close()

    c = open(file2, "r")
    c.write(str(b))
    c.close()


    c = open(file2, "r")
    print(c.read())
    c.close()