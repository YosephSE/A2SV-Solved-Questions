class Solution(object):
    def generate(self, numRows):
        res = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return res
        for i in range(numRows - 2):
            row = [1]
            for i in range(len(res[-1]) - 1):
                row.append(res[-1][i] + res[-1][i + 1])
            row.append(1)
            res.append(row)
        return res
