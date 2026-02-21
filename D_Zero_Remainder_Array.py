from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = map(int, input().split())
    remaining = {}

    for i in a:
        rem = i % k
        if rem != 0:
            remaining[k - rem] = remaining.get(k - rem, 0) + 1


    # x = 0
    # len_modes = len(remaining)
    # # while len_modes > 0:
    # for _ in range(2 * 10**5):
    #     if len_modes < 1:
    #         break
    #     key = x % k
    #     if key in remaining:
    #         remaining[key] -= 1

    #         if remaining[key] == 0:
    #             len_modes -= 1
    #     x += 1

    # print(x)





    