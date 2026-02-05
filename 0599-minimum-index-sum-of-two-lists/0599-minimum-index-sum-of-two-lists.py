class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        low_index = float('inf')
        word = []
        for i in list2:
            if i in list1:
                tot = list2.index(i) + list1.index(i)
                if tot == low_index:
                    low_index = tot
                    word.append(i)
                elif tot < low_index:
                    low_index = tot
                    word = [i]
        return word
        