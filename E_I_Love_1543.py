t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    
    ans = 0
    i = 0
    
    while i < n // 2 and i < m // 2:
        chars = []
        
        for col in range(i, m - i):
            chars.append(grid[i][col])
        
        for row in range(i + 1, n - i - 1):
            chars.append(grid[row][m - i - 1])
        
        for col in range(m - i - 1, i - 1, -1):
            chars.append(grid[n - i - 1][col])
        
        for row in range(n - i - 2, i, -1):
            chars.append(grid[row][i])
        
        s = "".join(chars)
        
        s += s[:3]
        
        ans += s.count("1543")
        
        i += 1
    
    print(ans)