t = int(input())
for _ in range(t):
    n = int(input())
    roots = []
    for i in range(n):
        roots.append(i + 1)
    print(' '.join(map(str, roots)))