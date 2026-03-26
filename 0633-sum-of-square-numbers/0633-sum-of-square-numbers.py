class Solution(object):
    def judgeSquareSum(self, c):
        sr = int(sqrt(c))

        for i in range(sr + 1):
            b = sqrt(c -(i * i))
            if b == int(b):
                return True
        return False
        