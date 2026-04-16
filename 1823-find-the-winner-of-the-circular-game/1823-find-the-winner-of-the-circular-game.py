class Solution(object):
    def findTheWinner(self, n, k):
        # init a list with range 1 to n
        a = list(range(1,n + 1))
        # loop and remove elements till we have one element left
        i = 0
        while len(a) > 1:
            i = (i + k - 1) % len(a)
            a.pop(i)



        return a[0]

        
        