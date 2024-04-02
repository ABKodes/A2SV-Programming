class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        size = len(piles)
        i = 0
        while i < size:
            if i >= size // 3:
                result += piles[i]
                i += 2
            else:
                i += 1
        return result
