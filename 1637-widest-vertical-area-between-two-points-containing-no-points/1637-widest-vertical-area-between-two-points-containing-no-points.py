class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort(key=lambda x: x[0])
        max_diff = 0
        for i in range(len(points) - 1):
            max_diff = max(max_diff, (points[i + 1][0] - points[i][0]))
        return max_diff
        