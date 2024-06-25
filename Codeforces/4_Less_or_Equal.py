n,k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
if k == 0:
    if min(arr) != 1:
        print(arr[0] -1)
    else:
        print("-1")
else:
    if k <= n:
        if k < n and arr[k] == arr[k-1]:
            print("-1")
        else:
            print(arr[k-1])
    else:
        print("-1")