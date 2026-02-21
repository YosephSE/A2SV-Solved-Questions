n, k = map(int, input().split())
lis = input().split()
kth_place_score = lis[k - 1]
for i in range(k - 1, n):
    if lis[i] < kth_place_score:
        print(i)
        break
else:
    print(0)


