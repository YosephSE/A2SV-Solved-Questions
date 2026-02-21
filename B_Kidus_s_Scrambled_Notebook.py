t = int(input())
for _ in range(t):
    ab = input()
    for i in range(1, len(ab)):
        str1 = ab[:i]
        str2 = ab[i:]
        num1 = int(str1)
        num2 = int(str2)
        if str1[0] != "0" and str2[0] != "0" and 0 < num1 < num2:
            print(f"{str1} {str2}")
            break
    else:
        print(-1)

