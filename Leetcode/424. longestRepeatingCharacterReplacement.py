class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxSubstring = 0
        left = 0
        # Dictionary to manage the maximum character
        counter = {chr(i): 0 for i in range(ord("A"), ord("Z") + 1)}
        for right in range(len(s)):
            counter[s[right]] += 1
            # If the window is invalid, shrink the window
            while (right - left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
            maxSubstring = max(maxSubstring, right - left + 1)
        return maxSubstring