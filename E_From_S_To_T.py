from collections import Counter

q = int(input())
for _ in range(q):
    s = input()
    t = input()
    p = input()
    i = 0
    j = 0
    while i < len(s):
        if j >= len(t) and i < len(s):
          print("NO")
          break
        elif s[i] == t[j]:
          i += 1
          j += 1
        else:
          j += 1
    else:
       req_count = Counter(t)
       ava_count = Counter(s + p)
       if ava_count >= req_count:
          print("YES")
       else:
          print("NO")
     
     
     
     

