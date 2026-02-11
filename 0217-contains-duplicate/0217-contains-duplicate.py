class Solution(object):
    def containsDuplicate(self, nums):
        freq = {}
        for i in nums:
            if i in freq:
                return True
            freq[i] = 1
        return False
            

        