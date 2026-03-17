class Solution(object):
    def runningSum(self, nums):
        prefix = 0
        for i in range(len(nums)):
            nums[i] += prefix
            prefix = nums[i]
        return nums

        