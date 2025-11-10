def nonDecreasing(n, m, a, b):
    prev = -float("inf")
    for i in range(n):
        keep = a[i]
        replace = b[0] - a[i]
        if keep >= prev and replace >= prev:
            chosen = min(keep, replace)
        elif keep >= prev:
            chosen = keep
        elif replace >= prev:
            chosen = replace
        else:
            return "NO"
        prev = chosen
    return "YES"
testCases = int(input())
for _ in range(testCases):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))  
    b = list(map(int, input().split()))
    print(nonDecreasing(n, m, a, b))

# a[i] choose to replace it with b[1] - a[i] or keep it.
