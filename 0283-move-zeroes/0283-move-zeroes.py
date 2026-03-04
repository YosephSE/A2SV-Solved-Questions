class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        while 0 in nums:
            nums.remove(0)
        nums.extend([0] *( n - len(nums)))

        # l, r = 0, 0
        # while r < len(nums):
        #     if 
        