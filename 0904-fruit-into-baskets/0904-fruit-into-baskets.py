class Solution(object):
    def totalFruit(self, fruits):
        res = 0
        f = defaultdict(int)
        l = 0
         
        for r in range(len(fruits)):
            f[fruits[r]] += 1

            while len(f) > 2:
                f[fruits[l]] -= 1
                if f[fruits[l]] == 0:
                    del f[fruits[l]]
                l += 1

            res = max(res, r - l + 1)

        return res
