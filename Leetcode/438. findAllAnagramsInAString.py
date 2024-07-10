class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        checker = Counter(p)
        k = len(p)
        result = []
        for i in range(len(s) - k + 1):
            window = s[i: k + i]
            if Counter(window) == checker:
                result.append(i)
        return result