w = int(input())
for i in range(2, (w // 2) + 1, 2):
    if (w - i) % 2 == 0:
        print("YES")
        break
else:
    print("NO")

