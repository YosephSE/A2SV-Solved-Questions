# def solve():
#     k = int(input())
#     s = input()
#     n = len(s)
#     left = 0
#     count = 0
#     ones = 0
#     result = 0

#     for right in range(n):
#         if s[right] == '1':
#             ones += 1

#         while ones > k and left <= right:
#             if s[left] == '1':
#                 ones -= 1
#             left += 1

#         if ones == k:
#             temp_left = left
#             temp_ones = ones
#             while temp_ones == k and temp_left <= right:
#                 result += 1
#                 if s[temp_left] == '1':
#                     temp_ones -= 1
#                 temp_left += 1

#     print(result)











from collections import defaultdict

def solve():
    k = int(input())
    s = input()
    prefix = [0] * (len(s) + 1)
    for i in range(len(s)):
        prefix[i+1] = prefix[i] + (1 if s[i] == '1' else 0)

    freq = defaultdict(int)
    freq[0] = 1
    result = 0

    for i in range(1, len(prefix)):
        result += freq.get(prefix[i] - k, 0)
        freq[prefix[i]] += 1

    print(result)











solve()



