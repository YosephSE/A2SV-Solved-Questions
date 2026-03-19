class Solution(object):
    def pivotIndex(self, nums):
        prefix = [0, nums[0]]
        total = sum(nums)
        print(total)
        

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        for i in range(1, len(prefix)):
            if total - prefix[i] == prefix[i - 1]:
                return i - 1
        return -1
        

        