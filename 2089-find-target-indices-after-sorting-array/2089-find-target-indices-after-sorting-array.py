class Solution(object):
    def targetIndices(self, nums, target):
        res = []
        freq = 0
        nums_less = 0
        for i in nums:
            if i == target:
                freq += 1
            elif i < target:
                nums_less += 1
        for i in range(freq):
            res.append(nums_less + i)
            
        return res
        
            

        