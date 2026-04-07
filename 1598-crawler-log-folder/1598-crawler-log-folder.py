class Solution(object):
    def minOperations(self, logs):
        stack = []
        for i in logs:
            if i == '../' and len(stack) > 0:
                stack.pop()
            elif i == '../':
                continue
            elif i == './':
                continue
            else:
                stack.append(i)
        return len(stack)

        