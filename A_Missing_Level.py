n = int(input())
a = (map(int, input().split()))
sum_a = sum(a)
missing_level = int(n * (n + 1) / 2) - sum_a
print(missing_level)
