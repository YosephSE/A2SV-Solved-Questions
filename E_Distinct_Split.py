from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    count = Counter(s)
    max_len = 0
    seen = set()
    for letter in s:
        seen.add(letter)
        count[letter] -= 1
        if count[letter] == 0:
            del count[letter]
        max_len = max(max_len, len(count) + len(seen))
    print(max_len)


