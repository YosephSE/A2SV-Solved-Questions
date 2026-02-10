t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    is_2025_in = "2025" in s
    is_2026_in = "2026" in s
    if is_2026_in:
        print(0)
    elif is_2025_in:
        print(1)
    else:
        print(0)
