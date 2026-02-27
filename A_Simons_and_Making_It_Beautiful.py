t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    max_elem, max_elem_index = float('-inf'), 0
    for i in range(n):
        if p[i] > max_elem:
            max_elem = p[i]
            max_elem_index = i
    
    p[0], p[max_elem_index] = p[max_elem_index], p[0]

    print(' '.join(map(str, p)))