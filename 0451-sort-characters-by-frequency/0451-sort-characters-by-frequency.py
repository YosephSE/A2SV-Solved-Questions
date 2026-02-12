class Solution(object):
    def frequencySort(self, s):
        freq = Counter(s)
        rev_freq = {}
        res = []
        for i in freq:
            if freq[i] in rev_freq:
                rev_freq[freq[i]].append(i)
            else:
                rev_freq[freq[i]] = [i]
        for i in sorted(rev_freq, reverse=True):
            word = map(lambda u: u * i, rev_freq[i])
            res.append(''.join(word))
        return ''.join(res)

        