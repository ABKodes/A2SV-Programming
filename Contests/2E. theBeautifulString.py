testCases = int(input())
for _ in range(testCases):
    s = list(input())
    q = int(input())
    for _ in range(q):
        i , v = input().split()
        i = int(i) - 1
        s[i] = v
        found = False
        for j in range(max(0, i-3), min(len(s) - 3, i + 1)):
            if s[j:j+4] == ["1", "1", "0", "0"]:
                found = True
                break
        print("YES" if found else "NO")
    