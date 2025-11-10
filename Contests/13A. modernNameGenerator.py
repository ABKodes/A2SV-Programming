testCases = int(input())
for _ in range(testCases):
    string = input()
    temp = string.split()
    stack = []
    for i in range(len(temp)):
        if temp[i] == "":
            continue
        else:
            stack.append(temp[i][0])
    print("".join(stack))