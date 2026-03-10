class Solution(object):
    def lengthOfLongestSubstring(self, s):
        unique = set()
        max_len = 0
        curr_len = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in unique:
                curr_len += 1
                max_len = max(max_len, curr_len)
                unique.add(s[r])
                r += 1

            else:
                unique.remove(s[l])
                l += 1
                curr_len -= 1
        return max_len

        
        