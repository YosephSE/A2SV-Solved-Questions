class Solution(object):
    def maxArea(self, height):
        max_con = 0
        l, r = 0, len(height) - 1

        while l < r:
            x = r - l
            y = min(height[l], height[r])
            max_con = max(max_con, x * y)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_con
        

        