class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_diff = float('inf')
        res = 0
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                if abs(tot - target) < closest_diff:
                    closest_diff = abs(tot - target)
                    res = tot
                if tot > target:
                    r -= 1
                elif tot <= target:
                    l += 1
        return res


        
        