class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        i = cur = 0
        for j in range(1, len(s)):
            cur += s[j] == s[j - 1]
            if cur > 1:
                i += 1
                cur -= s[i] == s[i - 1]
        return len(s) - i
        