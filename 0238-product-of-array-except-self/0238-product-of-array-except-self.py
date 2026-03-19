class Solution(object):
    def productExceptSelf(self, nums):
        res = [0] * len(nums)
        prefix = [1]
        postfix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i - 1])

        for i in range(len(nums) - 2, -1, -1):
            postfix.append(postfix[-1] * nums[i + 1])
        postfix.reverse()

        for i in range(len(prefix)):
            res[i] = prefix[i] * postfix[i]
        return res


        
        