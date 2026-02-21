t = int(input())

for _ in range(t):
    n = int(input())
    grid = [list(map(int, list(input().strip()))) for _ in range(n)]
    
    ans = 0
    
    for i in range(n):
        for j in range(n):
            ones = grid[i][j]
            ones += grid[j][n - 1 - i]
            ones += grid[n - 1 - j][i]
            ones += grid[n - 1 - i][n - 1 - j]
            
            ans += min(ones, 4 - ones)

    ans //= 4

    print(ans)
