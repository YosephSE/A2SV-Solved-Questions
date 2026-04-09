class Solution:
    def timeRequiredToBuy(self, tickets, k):
        val = tickets[k]
        res = 0
        for i in range(len(tickets)):
            if i < k:
                res += min(val, tickets[i])
            elif i == k:
                res += val
            elif i > k:
                res += min(val - 1, tickets[i])
        return res
