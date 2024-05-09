class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s = list(s)
        spaces = set(spaces)
        pointer = 0
        result = []
        while pointer < len(s):
            if pointer not in spaces:
                result.append(s[pointer])
            if pointer in spaces:
                result.append(" ")
                result.append(s[pointer])
            pointer +=1
        return ("").join(result)