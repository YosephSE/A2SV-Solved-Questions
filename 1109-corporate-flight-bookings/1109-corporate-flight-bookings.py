class Solution(object):
    def corpFlightBookings(self, bookings, n):
        res = []
        tot = 0
        prefix = [0] * (n + 1)

        for book in bookings:
            prefix[book[0] - 1] += book[2]
            prefix[book[1]] -= book[2]
        for i in range(len(prefix) - 1):
            tot += prefix[i]
            res.append(tot)

        return res

        