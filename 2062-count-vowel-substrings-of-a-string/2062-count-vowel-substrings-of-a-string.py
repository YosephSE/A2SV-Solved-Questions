class Solution:
    def countVowelSubstrings(self, word):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        last_seen = {}
        res = 0
        left = 0
        
        for right, ch in enumerate(word):
            if ch not in vowels:
                last_seen.clear()
                left = right + 1
                continue
            
            last_seen[ch] = right
            
            if len(last_seen) == 5:
                res += min(last_seen.values()) - left + 1
        
        return res