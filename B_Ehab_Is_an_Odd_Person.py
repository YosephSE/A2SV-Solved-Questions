n = int(input())
a = list(map(int, input().split()))

even_odd = [False, False]
for i in a:
    even_odd[i % 2] = True

if even_odd[0] and even_odd[1]:
    a.sort()

print(*a)