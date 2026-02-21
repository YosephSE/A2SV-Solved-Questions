def solve():
    n , m = map(int, input().split())
    diffs = []
    ori_files = []
    for _ in range(n):
        a, b = map(int, input().split())
        diffs.append(a - b)
        ori_files.append(a)

    sorted_diffs = sorted(diffs, reverse=True)
    sum_ori_files = sum(ori_files)
    comps = 0
    for i in range(len(sorted_diffs)):
        if sum_ori_files <= m:
            print(comps)
            return
        comps += 1
        sum_ori_files -= sorted_diffs[i]
    if sum_ori_files <= m:
            print(comps)
    else:
         print(-1)



solve()