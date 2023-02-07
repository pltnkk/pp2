def spy_game(nums):
    a = [0,0,7,'x']
    for num in nums:
        if num == a[0]:
            a.pop(0)
    return len(a) == 1

lst = list(map(int, input().split()))

print(spy_game(lst))