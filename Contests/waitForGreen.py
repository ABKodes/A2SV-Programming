numTestCases = int(input())
for _ in range(numTestCases):
    n, c = input().split()
    n = int(n)
    s = input().strip()

    if c == 'g':
        print(0)
        continue

    sExtended = s + s
    maxWaitTime = 0
    greenPos = -1

    for i in range(2 * n - 1, -1, -1):
        if sExtended[i] == 'g':
            greenPos = i
        
        if sExtended[i] == c and i < n and greenPos != -1:
            maxWaitTime = max(maxWaitTime, greenPos - i)
            
    print(maxWaitTime)
    
