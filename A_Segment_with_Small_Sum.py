n, s = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, 0
curr_sum = 0
max_len = 0

while r < n:
    if curr_sum + a[r] <= s:
        curr_sum += a[r]
        max_len = max(max_len, r - l + 1)
        r += 1
    else:
        curr_sum -= a[l]
        l += 1

print(max_len)