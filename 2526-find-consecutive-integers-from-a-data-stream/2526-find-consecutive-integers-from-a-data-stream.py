class DataStream(object):

    def __init__(self, value, k):
        self.value = value
        self.k = k
        self.lastDiff = 0
        self.size = 0
        

    def consec(self, num):
        self.size += 1

        if num != self.value:
            self.lastDiff = self.size

        return self.size - self.lastDiff >= self.k

        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)