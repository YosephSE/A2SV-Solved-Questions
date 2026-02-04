t = int(input())
for _ in range(t):
    n = int(input())
    str = input()
    freq = {}
    tot = 0
    for i in range(n):
        freq[str[i]] = freq.get(str[i], 0) + 1
    for i in freq:
        if freq[i] == 1:
            tot += 1
        else:
            tot += 2
    print(tot)




