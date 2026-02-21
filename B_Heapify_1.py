def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n // 2 + 2):
        if a[i - 1] > a[i]:
            a[i - 1], a[2 * i - 1] = a[2 * i - 1], a[i - 1]
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()