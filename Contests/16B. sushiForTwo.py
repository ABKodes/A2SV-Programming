n = int(input())
sushi = list(map(int, input().split()))

def isValidLength(length):
    if length % 2 != 0:
        return False
        
    halfLength = length // 2
    
    runs = []
    currentType = sushi[0]
    currentCount = 1
    
    for i in range(1, n):
        if sushi[i] == currentType:
            currentCount += 1
        else:
            runs.append((currentType, currentCount))
            currentType = sushi[i]
            currentCount = 1
    runs.append((currentType, currentCount))
    
    for i in range(len(runs) - 1):
        if runs[i][1] >= halfLength and runs[i+1][1] >= halfLength:
            return True
            
    return False

left, right = 2, n
if right % 2 != 0:
    right -= 1
    
result = 0
while left <= right:
    mid = (left + right) // 2
    if mid % 2 != 0:
        mid -= 1
        
    if mid == 0:
        break
        
    if isValidLength(mid):
        result = mid
        left = mid + 2
    else:
        right = mid - 2
print(result)
