t = int(input())
for _ in range(t):
    n, m, h = map(int, input().split())
    a = input().split()
    additional_value = [0] * n
    for i in range(m):
        b, c = map(int, input().split())
        additional_value[b - 1] += c
        if additional_value[b - 1] + int(a[b - 1]) > h:
            additional_value = [0] * n
    res = ' '.join([str(int(a[i]) + additional_value[i]) for i in range(n)])
    print(res)
        


