class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        i = 0
        j = 0
        count = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                count = count + 1
                i = i + 1
                j = j + 1
            else:
                j = j + 1
        return count