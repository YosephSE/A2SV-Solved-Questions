t = int(input())
for _ in range(t):
    no_of_piles = int(input())
    ops = 0
    for i in range(no_of_piles):
        a, b, c, d = map(int, input().split())
        if c < a:
            ops += a - c
        if d < b:
            ops += (min(a, c) + b - d)
    print(ops)
