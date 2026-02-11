from collections import Counter

class Solution(object):
    def findOriginalArray(self, changed):
        if len(changed) % 2 != 0:
            return []

        freq = Counter(changed)
        original = []

        for i in sorted(freq):
            if freq[i] == 0:
                continue

            if i == 0:
                if freq[i] % 2 != 0:
                    return []
                original.extend([0] * (freq[i] // 2))
            else:
                twice = i * 2
                if freq.get(twice, 0) < freq[i]:
                    return []
                original.extend([i] * freq[i])
                freq[twice] -= freq[i]

        return original
