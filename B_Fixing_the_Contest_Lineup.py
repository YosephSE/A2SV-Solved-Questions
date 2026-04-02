import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pa, pb = 0, 0
    res = 0

    while pb < n:
        if a[pa] <= b[pb]:
            pa += 1
            pb += 1
        else:
            res += 1
            pb += 1
    print(res)





t = int(input())
for _ in range(t):
    solve()