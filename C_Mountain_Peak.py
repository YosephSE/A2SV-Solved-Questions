import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    prefix_min = [-1] * n
    prefix_min_index = 0
    postfix_min = [-1] * n
    postfix_min_index = n - 1

    for i in range(1, n):
        if h[i] > h[prefix_min_index]:
            prefix_min[i] = prefix_min_index
        else:
            prefix_min_index = i
    for i in range(n - 2, -1, -1):
        if h[i] > h[postfix_min_index]:
            postfix_min[i] = postfix_min_index
        else:
            postfix_min_index = i
    
    for j in range(n):
        if prefix_min[j] != -1 and postfix_min[j] != -1:
            print("YES")
            print(prefix_min[j] + 1, j  + 1, postfix_min[j] + 1)
            return
    print("NO")




t = int(input())
for _ in range(t):
    solve()