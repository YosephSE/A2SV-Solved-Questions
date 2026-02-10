class Solution(object):
    def firstUniqChar(self, s):
        freq = Counter(s)
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        else:
            return -1
        