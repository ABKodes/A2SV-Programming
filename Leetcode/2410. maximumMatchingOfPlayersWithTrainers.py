class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        left = right = counter = 0
        while left < len(players) and right < len(trainers):
            if players[left] <= trainers[right]:
                left +=1
                right +=1
                counter += 1
            else:
                right +=1
        return counter
