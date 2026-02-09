class Solution(object):
    def majorityElement(self, nums):
        n = len(nums) / 3
        res = set()
        freq = {}
        for  i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq[i] > n:
                res.add(i)
        return list(res)
            
        