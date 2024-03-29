class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        temp = words[0]
        result = []
        for char in temp:
            if all(char in word for word in words[1:]):
                result.append(char)
                words[1:] = [word.replace(char, '', 1) for word in words[1:]]
        
        return result