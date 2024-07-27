class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/': 
                # If the token is an operation, pop the last two elements
                last,secondLast = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(last + secondLast)
                elif token == "-":
                    stack.append(secondLast - last)
                elif token == "*":
                    stack.append(last * secondLast)
                else:
                    division = secondLast / last
                    if division < 0:
                        stack.append(ceil(division))
                    else:
                        stack.append(floor(division))
            else:
                stack.append(int(token))
        return stack[0]