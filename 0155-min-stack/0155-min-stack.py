class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_elem = []
        

    def push(self, val):
        self.stack.append(val)
        if len(self.min_elem) > 0:
            self.min_elem.append(min(self.min_elem[-1], val))
        else:
            self.min_elem.append(val)
        
        

    def pop(self):
        self.stack.pop()
        self.min_elem.pop()
        
        

    def top(self):
        if len(self.stack):
            return self.stack[-1]
        return None

        
        

    def getMin(self):
        return self.min_elem[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()