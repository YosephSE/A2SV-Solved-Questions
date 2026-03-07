def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    skill_elite, skill_crowd = 0, 0
    count_elite, count_crowd = 0, 0
    l, r = 0, n - 1
    while l <= r:
        if skill_elite > skill_crowd and count_crowd > count_elite:
            print("YES")
            return
        elif skill_elite <= skill_crowd:
            skill_elite += a[r]
            count_elite += 1
            r -= 1
        elif count_elite >= count_crowd:
            skill_crowd += a[l]
            count_crowd += 1
            l += 1
    print("NO")






t = int(input())
for _ in range(t):
    solve()
