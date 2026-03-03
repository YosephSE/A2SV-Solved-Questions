class Solution(object):
    def findRelativeRanks(self, score):
        res = []
        sorted_score = sorted(score, reverse=True)
        rank = {}
        for i in range(len(sorted_score)):
            rank[sorted_score[i]] = i + 1
        for i in score:
            if rank[i] > 3:
                res.append(str(rank[i]))
            else:
                res.append(["Gold Medal", "Silver Medal", "Bronze Medal"][rank[i] - 1])
        return res
        