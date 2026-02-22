class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_elem = float('inf')
        

    def push(self, val):
        self.stack.append(val)
        self.min_elem = min(self.min_elem, val)
        
        

    def pop(self):
        self.stack.pop()
        
        

    def top(self):
        if len(self.stack):
            return self.stack[-1]
        return None

        
        

    def getMin(self):
        return min(self.stack)
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()