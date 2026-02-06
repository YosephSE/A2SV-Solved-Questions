n, m = map(int, input().split())
name = input()
replacements = {i: i for i in set(name)}
for i in range(m):
    s1, s2 = input().split()
    for key, value in replacements.items():
        if value == s1:
            replacements[key] = s2
        elif value == s2:
            replacements[key] = s1
res = []
for i in name:
    res.append(replacements[i])
print(''.join(res))
