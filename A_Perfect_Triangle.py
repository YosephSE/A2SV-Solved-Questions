t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    min_diff = float('inf')
    min_diff_index = None
    for i in range(1, n - 1):
        diff1 = a[i] - a[i - 1]
        diff2 = a[i + 1] - a[i]

        if diff1 + diff2 < min_diff:
            min_diff = diff1 + diff2
            min_diff_index = i
    print(min_diff)