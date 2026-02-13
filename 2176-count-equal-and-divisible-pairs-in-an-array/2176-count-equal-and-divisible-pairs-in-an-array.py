class Solution(object):
    def countPairs(self, nums, k):
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        return res
        