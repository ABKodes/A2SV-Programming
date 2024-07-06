testCases = int(input())
for _ in range(testCases):
    n = int(input())
    arr = list(map(int,input().split()))
    left = 0
    total = 0
    while left < n:
        right = left
        currentMax = arr[left]
        while right < n and (arr[right] > 0) == (arr[left] > 0):
            currentMax = max(currentMax,arr[right])
            right +=1
        total += currentMax
        left = right
    print(total)