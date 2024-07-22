class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        # Dictionary to keep the character and it's last index
        for index, char in enumerate(s):
            lastIndex[char] = index
        result = []
        size = 0
        end = 0
        for i in range(len(s)):
            size += 1
            end = max(end, lastIndex[s[i]])
            # If there's no occurrence
            if i == end:
                result.append(size)
                size = 0
        return result