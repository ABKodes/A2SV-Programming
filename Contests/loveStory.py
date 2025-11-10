checker = "codeforces"
testCases = int(input())
for _ in range(testCases):
    s = input()
    counter = 0
    for i in range(len(s)):
        if s[i] != checker[i]:
            counter += 1
    print(counter)
        