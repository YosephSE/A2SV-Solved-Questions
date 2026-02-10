class Solution(object):
    def do_math(self, n):
        tot = 0
        str_n = list(str(n))
        for i in str_n:
            tot += int(i)**2
        return tot

        
    def isHappy(self, n):
        while True:
            n = self.do_math(n)
            if n == 1:
                return True
            elif n == 4:
                return False

            


        
        