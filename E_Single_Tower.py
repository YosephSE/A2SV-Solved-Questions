def solve():
    line1 = input().split()
    n = int(line1[0])
    towers = []
    all_blocks = []
    for _ in range(n):
        data = list(map(int, input().split()))
        tower = data[1:]
        towers.append(tower)
        all_blocks.extend(tower)
    all_blocks.sort()
    successor = {}
    for i in range(len(all_blocks) - 1):
        successor[all_blocks[i]] = all_blocks[i+1]
    splits = 0
    total_segments = 0
    for tower in towers:
        # if not tower:
        #     continue

        segments_in_tower = 1
        for i in range(len(tower) - 1):
            top = tower[i]
            bottom = tower[i+1]
            if top not in successor or successor[top] != bottom:
                splits += 1
                segments_in_tower += 1
        
        total_segments += segments_in_tower
    combines = total_segments - 1
    print(splits, combines)


solve()