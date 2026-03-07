n = int(input())
a = list(map(int, input().split()))
s, d = 0, 0
l, r = 0, len(a) - 1
while l <= r:
    if a[l] > a[r]:
        s += a[l]
        l += 1
    else:
        s += a[r]
        r -= 1
    if l > r:
        break
    if a[l] > a[r]:
        d += a[l]
        l += 1
    else:
        d += a[r]
        r -= 1
print(s, d)
    

