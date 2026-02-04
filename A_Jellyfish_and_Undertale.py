t = int(input())
for _ in range(t):
    [a, b, n] = map(int, input().split())
    total_seconds = 0
    tools = list(map(int, input().split()))

    for i in range(n):
        if tools[i] < a:
            total_seconds += tools[i]
        elif tools[i] >= a:
            total_seconds += a - 1
    total_seconds += b
    print(total_seconds)
