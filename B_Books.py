n , t = map(int, input().split())
a = list(map(int, input().split()))

max_books = 0
curr_books = 0
curr_time = 0
l, r = 0, 0

while r < n:
    if curr_time + a[r] <= t:
        curr_books += 1
        max_books = max(max_books, curr_books)
        curr_time += a[r]
        r += 1
    else:
        curr_time -= a[l]
        curr_books -= 1
        l += 1
print(max_books)
