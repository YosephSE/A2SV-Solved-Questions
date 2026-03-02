class Solution(object):
    def runningSum(self, nums):
        res = []
        pre = 0
        for i in nums:
            pre += i
            res.append(pre)
        return res
        