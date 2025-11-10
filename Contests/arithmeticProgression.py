n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if n == 1:
    print(-1)
elif n == 2:
    a, b = arr
    d = b - a
    if d == 0:
        print(1)
        print(a)
    else:
        if d % 2 == 0:
            print(3)
            print(a - d, (a + b) // 2, b + d)
        else:
            print(2)
            print(a - d, b + d)
else:
    diffs = []
    for i in range(1, n):
        diffs.append(arr[i] - arr[i - 1])

    # Use set to see how many different differences exist
    unique_diffs = list(set(diffs))
    if len(unique_diffs) > 2:
        print(0)
    elif len(unique_diffs) == 1:
        d = unique_diffs[0]
        if d == 0:
            print(1)
            print(arr[0])
        else:
            print(2)
            print(arr[0] - d, arr[-1] + d)
    else:
        # Two different differences
        small = min(unique_diffs)
        big = max(unique_diffs)
        if big != 2 * small:
            print(0)
        else:
            # Try to find where the bigger gap is
            count = 0
            missing = -1
            for i in range(1, n):
                if arr[i] - arr[i - 1] == big:
                    count += 1
                    missing = arr[i - 1] + small
            if count == 1:
                print(1)
                print(missing)
            else:
                print(0)
