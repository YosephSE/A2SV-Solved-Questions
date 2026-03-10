class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    res += 1
                else:
                    break
        return res
        