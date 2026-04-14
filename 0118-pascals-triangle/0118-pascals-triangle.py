class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        res = [[1], [1, 1]]
        
        for i in range(2, numRows):
            prev = res[-1]
            toAppend = [1]
            for j in range(1, len(prev)):
                toAppend.append(prev[j - 1] + prev[j])
            toAppend.append(1)
            res.append(toAppend)
        
        return res