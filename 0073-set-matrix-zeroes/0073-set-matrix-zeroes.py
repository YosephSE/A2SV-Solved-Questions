class Solution(object):
    def setZeroes(self, matrix):
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols.add(i)
                    rows.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in cols or j in rows:
                    matrix[i][j] = 0



        
        