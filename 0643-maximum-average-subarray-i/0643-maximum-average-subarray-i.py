class Solution(object):
    def findMaxAverage(self, nums, k):
        curr = sum(nums[:k])
        max_sum = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr)

        return max_sum / float(k)