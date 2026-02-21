t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    max_no = max(a)
    print(max_no * n)