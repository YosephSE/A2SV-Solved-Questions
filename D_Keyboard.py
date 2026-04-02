
def solve():
    s = input()
    res = set()
    i = 0
    while i < len(s):
        if i + 1 < len(s) and  s[i] == s[i + 1]:
            i += 2
        else:
            res.add(s[i])
            i += 1




    print(''.join(sorted(res)))

t = int(input())
for _ in range(t):
    solve()