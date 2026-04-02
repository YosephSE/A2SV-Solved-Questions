def solve():
    n = int(input())
    s = input()
    l, r = 0, n - 1
    switch = 0
    while l < r:
        if switch == 0:
            if s[l] != s[r]:
                switch += 1
            r -= 1
            l += 1
        elif switch == 1:
            if s[l] == s[r]:
                switch += 1
            r -= 1
            l += 1
        elif switch == 2:
            if s[l] != s[r]:
                print("No")
                return
            r -= 1
            l += 1


    print("Yes")





t = int(input())
for _ in range(t):
    solve()