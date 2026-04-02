import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = [a[0]]
    for i in range(1, n):
        if b[-1] != a[i]:
            b.append(a[i])
    

    left,ans = 0,0
    for right in range(len(b)):
        if b[right] - b[left] >= n:
            left += 1
        ans = right - left + 1
    print(ans)


