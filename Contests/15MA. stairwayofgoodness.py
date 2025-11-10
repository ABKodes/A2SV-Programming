testCases = int(input())
for _ in range(testCases):
    left, right = map(int, input().split())
    difference = right - left
    low = 1
    high = 10**9
    bestNumber = 1
    while low <= high:
        mid = (low + high) // 2
        total = mid * (mid - 1) // 2 
        if total<= difference:
            bestNumber = mid
            low = mid + 1
        else:
            high = mid - 1
    print(bestNumber)
