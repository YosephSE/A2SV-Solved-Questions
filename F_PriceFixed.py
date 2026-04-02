limits = {}
for _ in range(int(input())):
    x,y = map(int,input().split())
    limits[y] = limits.get(y, 0) + x



count = sorted(limits.keys())

i, j = 0, len(count)-1

spent, purchased = 0,0
while i<=j:
    if count[i]<=purchased:
        spent += limits[count[i]]
        purchased += limits[count[i]]
        i+=1
    else:
        exp = count[i]
        diff = exp-purchased
        diff = min(exp-purchased,limits[count[j]])
        spent += 2*diff
        purchased += diff
        limits[count[j]]-=diff
        if limits[count[j]]==0:
            j-=1

print(spent)
