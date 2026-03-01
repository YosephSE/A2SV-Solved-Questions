n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
should_sub = 0
for i in a:
    if k <= 0:
        break
    if i - should_sub > 0:
        print(i - should_sub)
        should_sub += (i - should_sub)
        k -= 1

if k > 0:
    print('0\n' * k)
