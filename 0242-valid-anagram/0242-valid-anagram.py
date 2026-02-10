class Solution(object):
    def isAnagram(self, s, t):
        if Counter(t) == Counter(s):
            return True
        return False
        