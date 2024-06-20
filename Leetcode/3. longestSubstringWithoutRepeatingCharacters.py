class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = maxLength = 0
        seen = set()
        while left < len(s):
            char = s[left]
            while char in seen:
                seen.remove(s[right])
                right +=1
            seen.add(char)
            maxLength = max(maxLength,left-right+1)
            left +=1
        return maxLength