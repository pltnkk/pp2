import os


def createl(listt, myfile):
    file = open(myfile, "a")
    file.write(str(listt))
    file.close()

    file = open(myfile, "r")
    print(file.read())