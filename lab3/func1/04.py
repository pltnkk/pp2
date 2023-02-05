def filterprime(num):
    def isprime(n):
        if n <= 1:
            return False
        for i in range(2,n):
            if n % i == 0:
                return False

        return True

    return [n for n in num if isprime(n)]


print(filterprime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



