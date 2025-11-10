testCases = int(input())
for _ in range(testCases):
    word = input()
    checker = "yes"
    if checker.lower() in word.lower():
        print("YES")
    else:
        print("NO")