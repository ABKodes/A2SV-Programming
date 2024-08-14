class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Store the last occurrence index of each character
        lookUp = {s[i]: i for i in range(len(s))}

        stack = []  # Stack to build result
        seen = set()  # Track characters in stack

        for i in range(len(s)):
            if s[i] in seen:  # Skip if already in stack
                continue

            # Remove characters that are greater and appear later
            while stack and stack[-1] > s[i] and lookUp[stack[-1]] > i:
                seen.remove(stack.pop())

            # Add current character to stack
            seen.add(s[i])
            stack.append(s[i])

        return "".join(stack)
