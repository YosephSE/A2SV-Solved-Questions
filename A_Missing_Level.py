# n = int(input())
# a = (map(int, input().split()))
# sum_a = sum(a)
# missing_level = int(n * (n + 1) / 2) - sum_a
# print(missing_level)


n = int(input())
levels = list(map(int, input().split()))
 
for i in range(1,n):
    if i not in levels:
        print(i)
