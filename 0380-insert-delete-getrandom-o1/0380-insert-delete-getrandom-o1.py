class RandomizedSet(object):

    def __init__(self):
        self.the_set = set()
        self.the_list = []

        

    def insert(self, val):
        if val not in self.the_set:
            self.the_set.add(val)
            self.the_list.append(val)
            return True
        return False
     
    def remove(self, val):
        if val in self.the_set:
            self.the_set.remove(val)
            self.the_list.remove(val)
            return True
        return False
        

    def getRandom(self):
        list_len = len(self.the_list)
        random_index = random.randint(0, list_len - 1)
        return self.the_list[random_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()