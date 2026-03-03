class Solution(object):
    def maxCoins(self, piles):
        res = 0
        piles.sort()
        for i in range(len(piles) // 3, len(piles), 2):
            res += piles[i]
        return res

        