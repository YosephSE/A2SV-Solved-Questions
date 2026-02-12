class Solution(object):
    def minSteps(self, s, t):
        s_count = Counter(s)
        t_count = Counter(t)
        steps = 0
        for i in t_count:
            if t_count[i] > s_count.get(i, 0):
                steps += t_count[i] - s_count.get(i, 0)
        return steps



        