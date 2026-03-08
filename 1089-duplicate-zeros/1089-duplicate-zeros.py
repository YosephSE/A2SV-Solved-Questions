class Solution(object):
    def duplicateZeros(self, arr):
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr[i + 2:] = arr[i + 1:-1]
                arr[i + 1] = 0
                i += 2
            else:
                i += 1
        
        