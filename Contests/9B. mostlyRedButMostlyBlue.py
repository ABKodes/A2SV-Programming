testCases = int(input())
for _ in range(testCases):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)

    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + arr[i-1]
    reversedArr = arr[::-1]
    suffix = [0] * (n + 1)
    for i in range(1, n + 1):
        suffix[i] = suffix[i-1] + reversedArr[i-1]
    maxK = (n - 1) // 2
    found = False
    for k in range(1,maxK + 1):
        if prefix[k] > suffix[k + 1]:
            found = True
            break
    
    print("YES" if found else "NO")