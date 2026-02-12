class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        rans_count = Counter(ransomNote)
        mag_count = Counter(magazine)
        print(rans_count)
        print(mag_count)
        for i in rans_count:
            if rans_count[i] > mag_count.get(i, 0):
                return False
        return True
        