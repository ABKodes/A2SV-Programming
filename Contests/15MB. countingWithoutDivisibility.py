testCases = int(input())
for _ in range(testCases):
    n, k = map(int, input().split())
    left = 1
    right = 2 * k
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        count = mid - (mid // n)
        if count < k:
            left = mid + 1
        elif count > k:
            right = mid - 1
        else:
            if mid % n != 0:
                result = mid
                break
            else:
                right = mid - 1
    print(result if result else left)
