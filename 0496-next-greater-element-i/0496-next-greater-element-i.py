class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        mp = {}
        
        for i in range(len(nums2)):
            mp[nums2[i]] = -1
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    mp[nums2[i]] = nums2[j]
                    break
        return [mp[i] for i in nums1]
