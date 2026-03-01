# def solve():
#         n = int(input())
#         a = list(map(int, input().split()))
#         x = int(input())
#         for i in range(n - 1):
#             if min(a[i], a[i + 1]) <= x <= max(a[i], a[i + 1]):
#                 print("YES")
#                 return
#         print("NO")
#         return
# t = int(input())
# for _ in range(t):
#     solve()


def solve():
        n = int(input())
        a = list(map(int, input().split()))
        x = int(input())
        min_elem, max_elem = float('inf'), float('-inf')
        for i in range(n):
              min_elem = min(min_elem, a[i])
              max_elem = max(max_elem, a[i])
            
        if min_elem <= x <= max_elem:
              print("YES")
        else:
              print("NO")
t = int(input())
for _ in range(t):
    solve()
