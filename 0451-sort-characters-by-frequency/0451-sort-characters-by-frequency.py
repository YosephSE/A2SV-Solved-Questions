class Solution(object):
    def frequencySort(self, s):
        count = Counter(s)
        rev_count = defaultdict(list)
        for i in count:
            rev_count[count[i]].append(i)
        res = []
        for i in sorted(rev_count, reverse=True):
            for j in rev_count[i]:
                res.append(j * i)

        return ''.join(res)
        
