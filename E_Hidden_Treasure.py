def solve():
    n, m = map(int, input().split())
    min, max = 1, n

    for _ in range(m):
        clue = input().split()

        if clue[2] == 'left' and int(clue[-1]) - 1 < max:
            max = int(clue[-1]) - 1
        elif clue[2] == 'right' and int(clue[-1]) + 1 > min:
            min = int(clue[-1]) + 1
    if max < min:
        print(-1)
    else:
        print(max - min + 1)
        



solve()