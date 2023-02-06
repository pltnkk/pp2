from itertools import permutations

str = input()
def perr(string):
    for i in permutations(string):
        print(" ".join(i))

perr(str)
