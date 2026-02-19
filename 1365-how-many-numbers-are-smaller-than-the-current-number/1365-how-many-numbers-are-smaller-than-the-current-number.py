class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res = []
        for i in nums:
            res.append(len(filter(lambda x: x < i, nums)))
        return res
        