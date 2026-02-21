t = int(input())

for _ in range(t):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))
    
    total = sum(b) + s
    max_b = max(b)
    n = 1
    while n * (n + 1) // 2 < total:
        n += 1
    
    if n * (n + 1) // 2 == total and n >= max_b:
        print("YES")
    else:
        print("NO")
