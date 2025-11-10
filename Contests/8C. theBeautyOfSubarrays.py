testCases = int(input())
for _ in range(testCases):
    n = int(input())
    arr = list(map(int, input().split()))
    position = [0] * (n+1)
    result = []
    for index, value in enumerate(arr):
        position[value] = index 
    minValue = maxValue = position[1]
    for m in range(1, n+1):
        minValue = min(minValue, position[m])
        maxValue = max(maxValue, position[m])
        
        if maxValue - minValue + 1 == m:
            result.append('1')
        else:
            result.append('0')
    print(''.join(result))