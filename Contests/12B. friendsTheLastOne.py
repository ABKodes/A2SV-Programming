testCases = int(input())
for _ in range(testCases):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    if n > m:
        print("NO")
        continue
    
    sum_a = sum(a)
    max_a = max(a)
    
    if 2 * sum_a > m or max_a > (sum_a - max_a):
        print("NO")
    else:
        print("YES")