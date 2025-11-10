# Feasibility Checker
def isValid(n, m, k, x):
    rowCapacity = x * (m // (x + 1)) + (m % (x + 1))
    totalCapacity = n * rowCapacity
    return totalCapacity >= k
# Binary Search Function
def solve(n, m, k):
    low, high = 1, m
    answer = m
    
    while low <= high:
        mid = (low + high) // 2
        if isValid(n, m, k, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return answer

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    print(solve(n, m, k))
