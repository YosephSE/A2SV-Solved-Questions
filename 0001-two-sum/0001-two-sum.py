class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [i, hash_map[target - nums[i]]]
            else:
                hash_map[nums[i]] = i
            

        
        