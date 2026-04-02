import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        row = input().split()
        a.append(row)
    if len(a) > 1:
        temp = a[0]
        for i in range(len(a) - 1):
            a[i] = a[i + 1]
        a[-1] = temp
    else:
        if len(a[0]) < 2:
            print(-1)
            return
        else:
            temp = a[0][0]
            for i in range(len(a[0]) - 1):
                a[0][i] = a[0][i + 1]
            a[0][-1] = temp
    for row in a:
        print(*row)
    











t = int(input())
for _ in range(t):
    solve()