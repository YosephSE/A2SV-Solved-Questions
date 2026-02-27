class Solution(object):
    def longestCommonPrefix(self, strs):
        common = ""
        min_len = min(map(len, strs))
        for i in range(min_len):
            letter = strs[0][i]
            for j in strs:
                if j[i] != letter:
                    return common
            else:
                common += j[i]
        return common


        