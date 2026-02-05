class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        low_index = float('inf')
        word = []
        for i in list2:
            print("i:", i)
            if i in list1:
                tot = list2.index(i) + list1.index(i)
                print("tot:", tot)
                print("low_index:", low_index)
                if tot == low_index:
                    low_index = tot
                    word.append(i)
                    print("word:", word)
                elif tot < low_index:
                    low_index = tot
                    word = [i]
        return word
        