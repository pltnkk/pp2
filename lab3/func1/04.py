lst = map(int, input().split())

def isprime(x):
    x = int(x)
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False

    return True
def filter_prime(lst):
    x = []
    for i in lst:
        if isprime(i):
            x.append(i)
    return x


print(filter_prime(lst))



