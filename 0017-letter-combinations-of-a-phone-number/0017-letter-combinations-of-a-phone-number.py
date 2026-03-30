class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = [""]

        for digit in digits:
            temp = []
            for char in letterMap[digit]:
                for prev in res:
                    temp.append(prev + char)
            res = temp

        return res