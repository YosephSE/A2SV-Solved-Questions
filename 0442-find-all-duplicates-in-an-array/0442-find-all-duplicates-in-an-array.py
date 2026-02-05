class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        map = {}
        for i in nums:
            if i in map:
                res.append(i)
            else:
                map[i] = 1
        return res

            
        