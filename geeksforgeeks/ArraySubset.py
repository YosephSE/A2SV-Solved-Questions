#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        map_a = {}
        map_b = {}
        for i in a:
            map_a[i] = map_a.get(i, 0) + 1
        for i in b:
            map_b[i] = map_b.get(i, 0) + 1
        for i in map_b:
            if map_b[i] > map_a.get(i, 0):
                return False
        return True
            
            
        
        
    
    
