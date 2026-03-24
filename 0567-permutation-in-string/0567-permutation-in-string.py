class Solution(object):
    def checkInclusion(self, s1, s2):
        def compareCounter(c1, c2):
            for c in c1:
                if c1[c] != c2[c]:
                    return False
            return True
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        if compareCounter(s1_count, s2_count):
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            s2_count[s2[l]] -= 1
                
            l += 1
            s2_count[s2[r]] += 1

            if compareCounter(s1_count, s2_count):
                return True
        return False


