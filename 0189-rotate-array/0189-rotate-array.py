class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        res = []

        for i in range(-k, len(nums) - k):
            res.append(nums[i])

        nums[:] = res