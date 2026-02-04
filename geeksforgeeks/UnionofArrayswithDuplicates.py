class Solution:    
    def findUnion(self, a, b):
        set_a, set_b = set(a), set(b)
        return set_a.union(set_b)