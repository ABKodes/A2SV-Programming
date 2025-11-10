testCases = int(input())
for _ in range(testCases):
    n = int(input())
    a = list(map(int, input().split()))
    occupied = [False] * (n + 2)
    result = "YES"
    
    for i in range(n):
        seat = a[i]
        if i == 0:  # First passenger
            occupied[seat] = True
        else:
            if not (occupied[seat - 1] or occupied[seat + 1]):
                result = "NO"
                break
            occupied[seat] = True
            
    print(result)