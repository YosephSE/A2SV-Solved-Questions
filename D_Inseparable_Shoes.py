import sys
input = sys.stdin.readline


def solve():
    
        n = int(input())
        s = list(map(int, input().split()))
        
        ans = [0] * n
        i = 0
        
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            
            if j - i == 1:
                print(-1)
                return
            
            for k in range(i, j - 1):
                ans[k] = k + 2
            ans[j - 1] = i + 1
            # 1,2,3,4
            #4,1,2,3
            
            i = j
        
        print(*ans)

t = int(input())
for _ in range(t):
    solve()