n = 5
index_of_1 = 0
for i in range(n):
    col = input().split()
    if '1' in col:
        index_of_1 = (i, col.index('1'))
        break
print(abs(index_of_1[0] - 2) + abs(index_of_1[1] - 2))