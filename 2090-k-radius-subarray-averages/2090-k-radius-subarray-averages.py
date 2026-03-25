class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        res = [-1] * n
        
        if k == 0:
            return nums
        
        window_size = 2 * k + 1
        if window_size > n:
            return res
        
        window_sum = sum(nums[:window_size])
        
        for i in range(k, n - k):
            if i > k:
                window_sum += nums[i + k]
                window_sum -= nums[i - k - 1]
            
            res[i] = window_sum // window_size
        
        return res