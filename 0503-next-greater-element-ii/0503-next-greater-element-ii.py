class Solution(object):
    def nextGreaterElements(self, nums):
        res = [-1] * len(nums)
        stack = []

        for idx, val in enumerate(nums):

            while len(stack) != 0 and stack[-1][1] < val:
                popped = stack.pop()
                res[popped[0]] = val
            stack.append((idx, val))
            
        for val in nums:
            if len(stack) == 0:
                break
            while stack[-1][1] < val:
                popped = stack.pop()
                res[popped[0]] = val

        return res
            
        