class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l <= r:
            if ord(s[l]) < 48 or 57 < ord(s[l]) < 65 or 90 < ord(s[l]) < 97 or ord(s[l]) > 122:
                l += 1
            elif ord(s[r]) < 48 or 57 < ord(s[r]) < 65 or 90 < ord(s[r]) < 97 or ord(s[r]) > 122:
                r -= 1
            else:
                if ord(s[l].lower()) != ord(s[r].lower()):
                    return False
                l += 1
                r -= 1
        return True
        
        