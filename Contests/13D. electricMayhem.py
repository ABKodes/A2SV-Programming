s = input()
stack = []
for char in s:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)
print("Yes" if len(stack) == 0 else "No")