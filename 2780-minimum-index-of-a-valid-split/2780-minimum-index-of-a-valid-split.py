class Solution(object):
    def minimumIndex(self, nums):
        n = len(nums)
        count = Counter(nums)
        
        candidate = max(count, key=count.get)
        total = count[candidate]
        
        if total <= n // 2:
            return -1
        
        left_count = 0
        
        for i in range(n):
            if nums[i] == candidate:
                left_count += 1
            
            left_len = i + 1
            right_len = n - i - 1
            
            if left_count > left_len // 2 and (total - left_count) > right_len // 2:
                return i
        
        return -1
