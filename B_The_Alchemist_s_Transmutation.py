def solve():
        n = int(input())
        a = list(map(int, input().split()))
        x = int(input())
        min_elem, max_elem = min(a), max(a)
            
        if min_elem <= x <= max_elem:
              print("YES")
        else:
              print("NO")
t = int(input())
for _ in range(t):
    solve()
