class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        result,depth = 0,0
        for i in range(len(s)):
            if s[i] == '(':
                depth +=1 # Increase depth for '('
            else:
                depth -=1 # Decrease depth for ')'
                # Add score for a balanced string'()'
                if s[i-1] == '(':
                    result += 2**depth
        return result
            