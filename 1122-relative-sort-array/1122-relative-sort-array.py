class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        res = []
        unique = []
        arr2_set = set(arr2)
        count = Counter(arr1)
        for i in arr2:
            res.extend([i] * count[i])
        for i in count:
            if i not in arr2_set:
                unique.extend([i] * count[i])
        res.extend(sorted(unique))
        return res
        