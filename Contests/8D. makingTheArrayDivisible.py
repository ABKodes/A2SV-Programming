testCases = int(input())
for _ in range(testCases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    required = {}
    
    for num in arr:
        remainder = num % k
        if remainder != 0:
            increment = k - remainder
            if increment in required:
                required[increment] += 1
            else:
                required[increment] = 1
    
    if not required:
        print(0)
    else:
        max_moves = 0
        for increment, count in required.items():
            moves = (count - 1) * k + increment + 1
            max_moves = max(max_moves, moves)
        
        print(max_moves)