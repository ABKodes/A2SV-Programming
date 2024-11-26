def maxProblems(n,k):
    maxTime = 240 - k
    left,right = 0,n
    result = 0
    
    while left <= right:
        mid = (left + right)//2
        timeRequired = 5 * (mid * (mid + 1))//2
        if timeRequired <= maxTime:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
            
    return result

n,k = map(int,input().split())
print(maxProblems(n,k))