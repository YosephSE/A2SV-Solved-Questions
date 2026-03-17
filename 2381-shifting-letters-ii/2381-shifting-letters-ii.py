class Solution(object):
    def shiftingLetters(self, s, shifts):
        prefix = [0] * len(s)
        res = []
        for shift in shifts:

            prefix[shift[0]] += (1 if shift[2] == 1 else -1)
            if len(prefix) - 1 >= shift[1] + 1:
                prefix[shift[1] + 1] += (-1 if shift[2] == 1 else 1)
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        for i in range(len(s)):
            ord_val = (ord(s[i]) - ord('a') + prefix[i]) % 26 + ord('a')
            char = chr(ord_val)
            res.append(char)
        return ''.join(res)
