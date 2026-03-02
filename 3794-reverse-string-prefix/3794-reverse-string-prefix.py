class Solution(object):
    def reversePrefix(self, s, k):
        s1 = list(s[:k])
        s1.reverse()
        return "".join(s1) + s[k:]

        