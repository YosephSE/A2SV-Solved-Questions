class Solution(object):
    def countNegatives(self, grid):
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    res += 1
        return res
        