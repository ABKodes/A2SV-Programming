testCases = int(input())
for _ in range(testCases):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n == 1:
        print("YES")
        continue
    
    arr.sort()
    flag = True
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) > 1:
            flag = False
            break
    
    print("YES" if flag else "NO")
