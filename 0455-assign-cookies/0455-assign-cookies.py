class Solution(object):
    def findContentChildren(self, g, s):
        res = 0
        g.sort()
        s.sort()
        gp, sp = 0, 0

        while gp < len(g) and sp < len(s):
            if g[gp] <= s[sp]:
                res += 1
                gp += 1
                sp += 1
            else:
                sp += 1
        return res



        