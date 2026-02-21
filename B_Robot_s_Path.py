n, k = map(int, input().split())
a = input()
def solve(n, k, a):
    max_obstacles = 0
    curr_obstacles = 0
    for i in a:
        if max_obstacles >= k:
            print('NO')
            return
        if i == ".":
            max_obstacles = max(max_obstacles, curr_obstacles)
            curr_obstacles = 0
        elif i == '#':
            curr_obstacles += 1

    if max_obstacles >= k:
        print("NO")
    else:
        print("YES")
    return

solve(n, k, a)

