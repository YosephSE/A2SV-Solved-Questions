class Solution(object):
    def restoreString(self, s, indices):
        res = ['0'] * len(indices)
        for i in range(len(indices)):
            res[indices[i]] = s[i]

        return ''.join(res)
        