def small_ord(str1, str2):
    tot_ord = 0
    max_len = max(len(str1), len(str2))
    for i in range(max_len):
        if i >= len(str1):
            return True
        elif i >= len(str2):
            return False
        elif ord(str1[i]) < ord(str2[i]):
            return True
        elif ord(str1[i]) > ord(str2[i]):
            return False





t = int(input())
for i in range(t):
    n = int(input())
    strs = input().split()
    s = ''
    for j in range(n):
        if small_ord(s + strs[j], strs[j] + s):
            s += strs[j]
        else:
            s = strs[j] + s
    print(s)

