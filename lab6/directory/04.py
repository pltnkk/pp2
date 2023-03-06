import os 

def count(name):
    cnt = 0
    file = open(name, "r")
    for i in file:
        cnt = cnt + 1

    return cnt