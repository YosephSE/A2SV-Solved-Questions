n = int(input())
a = list(map(int, input().split()))

def count_greater_values(lis, val):
    no_of_greater_scores = 0
    for i in range(len(a)):
        if lis[i] > val:
            no_of_greater_scores += 1
    return no_of_greater_scores
positions = []

                   
for i in a:
    position = count_greater_values(a, i) + 1
    positions.append(str(position))

print(' '.join(positions))