class Solution(object):
    def rotate_90(self, mat, target):
        rotated = [list(row)[::-1] for row in zip(*mat)]
        return rotated == target
        
    def rotate_180(self, mat, target):
        rotated = [row[::-1] for row in mat[::-1]]
        return rotated == target

    def rotate_270(self, mat, target):
        rotated = list(zip(*mat))[::-1]
        rotated = [list(row) for row in rotated]
        return rotated == target

    def findRotation(self, mat, target):
        if mat == target:
            return True
        
        if (self.rotate_90(mat, target) or 
            self.rotate_180(mat, target) or 
            self.rotate_270(mat, target)):
            return True
        
        return False
