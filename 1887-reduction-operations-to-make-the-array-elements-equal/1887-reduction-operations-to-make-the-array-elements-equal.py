class Solution(object):
    def reductionOperations(self, nums):
        res = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                res += len(nums) - i
        return res

        
        
        