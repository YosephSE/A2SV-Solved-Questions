class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    if a * b < 0:
                        stack.append(- (abs(a) // abs(b)))
                    else:
                        stack.append(a // b)
            else:
                stack.append(int(i))
        return stack[0]