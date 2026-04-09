class Solution(object):
    def dailyTemperatures(self, t):
        stack = []
        res = [0] * len(t)

        for i in range(len(t)):
            while len(stack) > 0 and stack[-1][1] < t[i]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, t[i]))
        return res

        