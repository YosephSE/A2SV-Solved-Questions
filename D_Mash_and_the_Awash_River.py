
from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    if "**" in s or ">*" in s or "*<" in s  or "><" in s:
        print(-1)
    else:
       count = Counter(s)
       n = len(s)
       res = n - min(count[">"], count["<"])
       print(res)


