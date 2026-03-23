class Solution:
    def maximumSubarraySum(self, nums, k):
        maximum = 0
        count = Counter(nums[:k])
        tot = sum(nums[:k])
        if len(count) == k:
            maximum = tot
        left = 0
        for right in range(k, len(nums)):
            count[nums[left]] -= 1
            tot -= nums[left]
            if count[nums[left]] == 0:
                count.pop(nums[left])
            left += 1
            count[nums[right]] += 1
            tot += nums[right]

            if len(count) == k:
                maximum = max(maximum, tot)
        return maximum
            
        