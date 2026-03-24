from collections import defaultdict

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        res = curr = 0
        seen = set()
        l = 0

        for r in range(len(nums)):

            while nums[r] in seen:
                seen.remove(nums[l])
                curr -= nums[l]
                l += 1

            curr += nums[r]
            seen.add(nums[r])
            res = max(res, curr)

        return res