import os 


for char in range(ord("A"), ord("Z") + 1):
    wordfile = "{}.txt"
    file = open(wordfile.format(chr(char)), "x")