class Solution(object):
    def productExceptSelf(self, nums):
        res = []
        pre_mul = [1]
        post_mul = [1]

        for i in range(len(nums) - 1):
            pre_mul.append(pre_mul[-1] * nums[i])

        for i in range(len(nums) - 1, 0, -1):
            post_mul.append(post_mul[-1] * nums[i])

        post_mul.reverse()
        
        for i in range(len(pre_mul)):
            res.append(pre_mul[i] * post_mul[i])

        return res
        
        
        