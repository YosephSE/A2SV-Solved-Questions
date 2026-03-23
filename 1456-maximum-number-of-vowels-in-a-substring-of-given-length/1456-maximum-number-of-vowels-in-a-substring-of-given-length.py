class Solution(object):
    def maxVowels(self, s, k):
        max_ = 0
        l = 0
        curr = 0
        vowels = 'aeiou'
        for r in range(len(s)):
            if s[r] in vowels:
                curr += 1
                max_ = max(curr, max_)
            if r - l + 1 == k:
                if s[l] in vowels:
                    curr -= 1
                l += 1
        return max_
        

        
        