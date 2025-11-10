def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True
testCases = int(input())
for _ in range(testCases):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(len(arr)):
        if is_sorted(arr):
            flag = False
            break
    print("YES" if flag else "NO")