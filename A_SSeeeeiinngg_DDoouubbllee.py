t = int(input())
for _ in range(t):
    s = input()
    res = list(s)
    res.extend(reversed(s))

    print(''.join(res))

    