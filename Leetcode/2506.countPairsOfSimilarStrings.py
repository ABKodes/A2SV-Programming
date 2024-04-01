class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        size = len(words)
        for i in range(0,size,1):
            for j in range(i+1,size,1):
                if set(words[i]) == set(words[j]):
                    count += 1
        return count