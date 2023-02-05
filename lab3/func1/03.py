numheads = int(input())
numlegs = int(input())
def solve(numheads, numlegs):
    for chic in range(numheads + 1):
        rabb = numheads - chic
        if 2 * chic + 4 * rabb == numlegs:
            print(chic, rabb)
    

solve(numheads,numlegs)