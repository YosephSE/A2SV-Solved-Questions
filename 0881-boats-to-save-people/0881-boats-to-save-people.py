class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()

        res = 0
        l, r = 0, len(people) - 1

        while l <= r:
            if l == r:
                return res + 1
            if people[r] + people[l] <= limit:
                res += 1
                r -= 1
                l += 1
            else:
                res += 1
                r -= 1
        return res