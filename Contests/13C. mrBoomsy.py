testCases = int(input())
for _ in range(testCases):
    string = input()
    stack = []
    for char in string:
        if stack:
            if stack[-1] == "A" and char == "B" or stack[-1] == "B" and char == "B":
                stack.pop()
                continue
        stack.append(char)
    print(len(stack))