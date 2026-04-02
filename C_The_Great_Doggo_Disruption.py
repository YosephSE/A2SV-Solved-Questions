

def solve():
    lis = [0] * 26
    n = int(input())
    s = input()
    if n == 1:
        print("Yes")
        return
    for c in s:
        idx = ord(c) - 97 # ord('a')
        lis[idx] += 1
        if lis[idx] >= 2:
            print("Yes")
            return
    print('No')

solve()