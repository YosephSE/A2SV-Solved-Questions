class Solution(object):
    def topKFrequent(self, nums, k):
        res = []
        count = Counter(nums)
        rev_freq = {}
        for i in count:
            if count[i] in rev_freq:
                rev_freq[count[i]].append(i)
            else:
                rev_freq[count[i]] = [i]
        for i in sorted(rev_freq, reverse=True):
            res.extend(rev_freq[i])

        return res[:k]



        
        