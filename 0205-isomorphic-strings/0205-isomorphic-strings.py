class Solution(object):
    def isIsomorphic(self, s, t):
        char_map = {}
        char_set = set()
        for i in range(len(s)):
            if s[i] in char_map and char_map[s[i]] != t[i]:
                return False
            elif s[i] in char_map and char_map[s[i]] == t[i]:
                continue
            # elif s[i] == t[i]:
            #     return False
            elif t[i] in char_set:
                return False
            else:
                char_map[s[i]] = t[i]
                char_set.add(t[i])
        return True
            
                
        