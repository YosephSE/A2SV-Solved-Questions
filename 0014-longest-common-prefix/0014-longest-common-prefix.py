class Solution(object):
    def longestCommonPrefix(self, strs):
        common = strs[0]
        for i in range(len(common)):
            for j in range(1, len(strs)):
                if  i == len(strs[j]) or  common[i] != strs[j][i]:
                    return common[:i]
        return common
        