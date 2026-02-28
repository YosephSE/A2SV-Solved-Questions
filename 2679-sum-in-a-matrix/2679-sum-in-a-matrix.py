class Solution(object):
    def matrixSum(self, nums):
        res = 0
        for i in nums:
            i.sort()
        for k in range(len(nums[0])):
            max_elem = 0
            for i in nums:
                max_elem = max(max_elem, i.pop())
            res += max_elem
        return res
        


            
            


        
        