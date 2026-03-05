class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        res = 0
        players.sort()
        trainers.sort()
        j = 0
        for i in players:
            while len(trainers) > j:
                if i <= trainers[j]:
                    res += 1
                    j += 1
                    break
                j += 1
        return res
            
            



        