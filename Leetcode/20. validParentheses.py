class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"[": "]", "(": ")", "{": "}"}
        for i in range(len(s)):
            if s[i] in brackets.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if s[i] != brackets[top]:
                    return False
        return len(stack) == 0
