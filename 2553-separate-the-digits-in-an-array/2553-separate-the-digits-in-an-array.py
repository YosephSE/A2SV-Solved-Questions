class Solution(object):
    def separateDigits(self, nums):
        res = []
        for i in nums:
            res.extend(list(str(i)))
        res = map(int, res)
        return res
        