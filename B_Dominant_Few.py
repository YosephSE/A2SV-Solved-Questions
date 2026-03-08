def solve():
    n = int(input())
    a = sorted(map(int, input().split()))

    crowd = a[0]
    elite = 0

    for i in range(1, n):
        crowd += a[i]
        elite += a[n-i]

        if elite > crowd and i < n-i:
            print("YES")
            return

    print("NO")


t = int(input())
for _ in range(t):
    solve()