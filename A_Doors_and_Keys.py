t = int(input())
for _ in range(t):
    str = input()
    if str.index("r") < str.index("R") and str.index("g") < str.index("G") and str.index("b") < str.index("B"):
        print("YES")
    else:
        print("NO")