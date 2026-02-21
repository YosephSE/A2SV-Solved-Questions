class Solution(object):
    def isValid(self, s):
        stack = []
        map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif stack.pop() != map[i]:
                    return False
        if len(stack) > 0:
            return False
        return True
                

        