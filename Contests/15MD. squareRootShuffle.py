for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        arr = []
        for i in range(n // 2, n // 2 + n + 1):
            if i != n:
                arr.append(i)
        print(*arr)
    else:
        arr = []
        for i in range(n // 2 + 3, n // 2 + 3 + n):
            arr.append(i)
        arr[0] -= 1
        arr[-1] += 1
        arr[-2] += 1
        print(*arr)