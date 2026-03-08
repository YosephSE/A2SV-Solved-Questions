class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        res = []
        first, second = 0, 0
        while first < len(firstList) and second < len(secondList):
            low = max(firstList[first][0], secondList[second][0])
            high = min(firstList[first][1], secondList[second][1])
            if low <= high:
                res.append([low, high])
            if firstList[first][1] > secondList[second][1]:
                second += 1
            else:
                first += 1
        return res
        
        