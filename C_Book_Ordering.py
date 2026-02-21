def solve():
    n = int(input())
    lis = [float('inf')]
    for _ in range(n):
        w, h = map(int, input().split())
        if max(w, h) <= lis[-1]:
            lis.append(max(w, h))
        elif min(w, h) <= lis[-1]:
            lis.append(min(w, h))
        elif h > lis[-1] and w > lis[-1]:
            print('NO')
            return
        
    print("YES")

        


solve()