class Solution(object):
    def maximumUniqueSubarray(self, nums):
        res = curr = 0
        unique = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            curr += nums[r]
            unique[nums[r]] += 1
            while unique[nums[r]] > 1:
                unique[nums[l]] -= 1
                curr -= nums[l]
                if unique[nums[l]] == 0:
                    unique.pop(nums[l])
                l += 1
            res = max(res, curr)
        return res                
                







        
        