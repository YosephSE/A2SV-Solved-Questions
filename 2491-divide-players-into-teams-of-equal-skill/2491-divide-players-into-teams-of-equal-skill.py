class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        chem = 0
        team_skill = skill[0] + skill[-1]
        l, r = 0, len(skill) - 1
        while l < r:
            if skill[l] + skill[r] != team_skill:
                return -1

            chem += (skill[l] * skill[r])
            l += 1
            r -= 1
        return chem


        
        