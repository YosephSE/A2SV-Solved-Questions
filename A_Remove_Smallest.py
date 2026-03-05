def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n < 2:
        print("YES")
        return
    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            print("NO")
            return
    print("YES")



t = int(input())
for _ in range(t):
    solve()