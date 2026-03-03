class Solution(object):
    def smallestNumber(self, num):
        if num < 0:
            res = sorted(str(num), reverse=True)[:-1]
            return int(''.join(['-'] + res))
        elif num > 0:
            res = ''.join(sorted(str(num)))
            zeros = res.count('0')
            res = int(res[zeros] + '0' * zeros + res[zeros + 1:])
            return res

        else:
            return 0

        
        