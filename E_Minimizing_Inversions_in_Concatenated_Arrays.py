t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    a.sort(key=lambda i: i[0] + i[1])
    res = []
    for i in a:
        res.append(str(i[0]) + ' ' + str(i[1]) + ' ')
    print(''.join(res))
