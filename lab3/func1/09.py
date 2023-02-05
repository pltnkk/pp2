import math

def volume(rad):
    return (4/3) * math.pi * (rad ** 3)

rad = int(input())
print(volume(rad))