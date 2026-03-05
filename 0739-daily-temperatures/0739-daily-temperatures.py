class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                stackInd, stackT = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((i, val))
        return res