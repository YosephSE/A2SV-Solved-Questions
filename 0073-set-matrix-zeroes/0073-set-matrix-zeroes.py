class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):

                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[i][k] != 0:
                            matrix[i][k] = float("inf")

                    for k in range(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = float("inf")


        for i in range(n):
            for j in range(m):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0

        


        