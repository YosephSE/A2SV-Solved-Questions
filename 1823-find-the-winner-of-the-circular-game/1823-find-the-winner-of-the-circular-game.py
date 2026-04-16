class Solution:
    def findTheWinner(self, n, k):
        return self.winnerHelper(n, k) + 1

    def winnerHelper(self, n, k):
        if n == 1:
            return 0
        return (self.winnerHelper(n - 1, k) + k) % n