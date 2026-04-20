class Solution(object):
    def clearDigits(self, s):
        stack = []
        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for c in s:
            if c in digits and len(stack) > 0:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

        
        