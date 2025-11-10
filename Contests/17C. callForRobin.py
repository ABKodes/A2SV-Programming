for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 0:
        print(-1)
        continue
    
    maxOriginalWealth = arr[0]
    for val in arr:
        if val > maxOriginalWealth:
            maxOriginalWealth = val
    
    originalTotalWealth = sum(arr)

    def check(currentX):
        newTotalWealth = originalTotalWealth + currentX
        newAverageWealth = newTotalWealth / n
        discontentThreshold = newAverageWealth / 2.0

        discontentCitizensCount = 0
        bonusAppliedToOneMax = False

        for wealthVal in arr:
            if wealthVal == maxOriginalWealth and not bonusAppliedToOneMax:
                bonusAppliedToOneMax = True
            else:
                if wealthVal < discontentThreshold:
                    discontentCitizensCount += 1
        
        return discontentCitizensCount * 2 > n
        
    left = 0
    right = 4 * (10**11) 
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            result = mid
            right = mid - 1 
        else:
            left = mid + 1
            
    print(result)