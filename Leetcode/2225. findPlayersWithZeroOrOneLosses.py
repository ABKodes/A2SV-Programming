class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnerDict = {}
        loserDict = {}
        winner = []
        oneloss = []
        for i in range(len(matches)):
            winnerDict[matches[i][0]] = winnerDict.get(matches[i][0], 0) + 1
            loserDict[matches[i][1]] = loserDict.get(matches[i][1], 0) + 1
        for key in winnerDict:
            if key not in loserDict:
                winner.append(key)
        for key,value in loserDict.items():
            if value == 1:
                oneloss.append(key)
        winner.sort()
        oneloss.sort()
        return [winner,oneloss]