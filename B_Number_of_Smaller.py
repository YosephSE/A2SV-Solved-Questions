n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []
nums_less = 0

for i in b:
    while nums_less < n and a[nums_less] < i:
        nums_less += 1
    res.append(nums_less)

print(*res)