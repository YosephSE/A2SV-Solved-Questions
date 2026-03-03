n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
should_sub = 0
# 3,3,5,10
for i in a:
    if k <= 0:
        break
    if i - should_sub > 0: #it is the min non zero element
        print(i - should_sub)
        # should_sub += (i - should_sub)
        should_sub = i
        k -= 1

if k > 0:
    print('0\n' * k)
