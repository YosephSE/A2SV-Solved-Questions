class Solution(object):
    def twoSum(self, nums, target):
        visited = {}
        for i in range(len(nums)):
            if target - nums[i] in visited:
                return [visited[target - nums[i]], i]
            visited[nums[i]] = i
        