class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False
        word1_count = Counter(word1)
        word2_count = Counter(word2)
        count1 = list(word1_count.values())
        count2 = list(word2_count.values())
        return sorted(count1) == sorted(count2) and set(word1) == set(word2)
