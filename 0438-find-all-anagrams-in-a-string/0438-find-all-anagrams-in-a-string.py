class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        p_counter = Counter(p)
        s_counter = Counter()
        l = 0
        for r in range(len(s)):
            s_counter[s[r]] += 1
            # print('-----')
            # print(s_counter)
            # print(p_counter)
            # print(l)
            if p_counter == s_counter:
                res.append(l)
            if r - l + 1 == len(p):
                s_counter[s[l]] -= 1
                if s_counter[s[l]] == 0:
                    del s_counter[s[l]]
                l += 1
        return res


        
        