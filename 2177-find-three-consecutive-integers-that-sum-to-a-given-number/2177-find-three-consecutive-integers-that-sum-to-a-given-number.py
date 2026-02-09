class Solution(object):
    def sumOfThree(self, num):
        if num % 3 == 0:
            ave = num / 3
            return [ ave - 1, ave, ave + 1]
        return []
        
        