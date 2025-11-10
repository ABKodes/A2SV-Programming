testCases = int(input())
for _ in range(testCases):
    n = int(input())
    result = (n // 4) + ((n % 4)//2)
    print(result)
