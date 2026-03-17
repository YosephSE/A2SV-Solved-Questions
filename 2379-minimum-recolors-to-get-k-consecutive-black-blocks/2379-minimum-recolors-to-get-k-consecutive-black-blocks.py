class Solution(object):
    def minimumRecolors(self, blocks, k):
        freq = Counter(blocks[:k])
        min_ = freq['W']
        l = 0
        for r in range(k, len(blocks)):
            freq[blocks[r]] += 1
            freq[blocks[l]] -= 1
            l += 1
            min_ = min(min_, freq['W'])
        return min_


        
        