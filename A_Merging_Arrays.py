n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ap, bp = 0, 0
res = []
while True:
    if ap >= len(a) and bp >= len(b):
        break
    elif ap >= len(a):
        res.append(b[bp])
        bp += 1
    elif bp >= len(b):
        res.append(a[ap])
        ap += 1
    else:
        if a[ap] < b[bp] :
            res.append(a[ap])
            ap += 1
        elif a[ap] >= b[bp]:
            res.append(b[bp])
            bp += 1



print(* res)