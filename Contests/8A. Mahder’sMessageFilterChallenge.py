testCases = int(input())
for _ in range(testCases):
    n = int(input())
    s = input()
    total = 0
    i = len(s) - 1
    while i >=0 and s[i] == ")":
        total += 1
        i -= 1
    print("Yes" if total > (len(s) - total) else "No" )