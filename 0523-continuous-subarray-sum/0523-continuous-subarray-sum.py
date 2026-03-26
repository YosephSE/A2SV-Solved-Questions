class Solution(object):
    def checkSubarraySum(self, nums, k):
        total = 0
        reminders = {0: -1}
        for i, n in enumerate(nums):
            total += n
            if total % k not in reminders:
                reminders[total % k] = i
            elif i - reminders[total % k] > 1:
                return True
        return False
            
        
        
        