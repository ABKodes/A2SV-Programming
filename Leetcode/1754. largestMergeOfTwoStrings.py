class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        merge = ""
        while left < len(word1) and right < len(word2):
            if word1[left] > word2[right]:
                merge += word1[left]
                left += 1
            elif word1[left] < word2[right]:
                merge += word2[right]
                right += 1
            else:
                if left < len(word1) and right < len(word2) and word1[left] == word2[right]:
                    if word1[left:] > word2[right:]:
                        merge += word1[left]
                        left += 1
                    else:
                        merge += word2[right]
                        right += 1
        merge += word1[left:]
        merge += word2[right:]
        return merge