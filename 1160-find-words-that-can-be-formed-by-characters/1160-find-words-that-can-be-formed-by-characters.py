class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        tot = 0
        for i in words:
            i_count = Counter(i)
            if chars_count >= i_count:
                tot += len(i)
        return tot
        