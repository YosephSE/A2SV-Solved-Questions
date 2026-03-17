class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        prefix = [0] * (n + 1)
        res = []
        base = ord('a')

        for left, right, direction in shifts:
            prefix[left] += 1 if direction == 1 else -1
            prefix[right + 1] += -1 if direction == 1 else 1

        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        for i in range(n):
            ord_val = (ord(s[i]) - base + prefix[i]) % 26 + base
            res.append(chr(ord_val))

        return ''.join(res)
