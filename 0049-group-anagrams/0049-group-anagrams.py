class Solution(object):
    def groupAnagrams(self, strs):
        map = {}
        for i in strs:
            sorted_i = ''.join(sorted(i))
            if sorted_i not in map:
                map[sorted_i] =[]
            map[sorted_i].append(i)
        res = (map.values())
        return res

        