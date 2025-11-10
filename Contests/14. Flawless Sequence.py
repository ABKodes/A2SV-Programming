import math

def check(k):
    j = int(math.isqrt(k * (k + 1) // 2))
    return j * j != k * (k + 1) // 2

    


testCases = int(input())
for _ in range(testCases):
    n = int(input())
    if not check(n):
        print(-1)
        continue

    ans = list(range(n + 2))

    j = 0
    for i in range(1, n + 1):
        while j * j < i * (i + 1) // 2:
            j += 1
        if j * j == i * (i + 1) // 2:
            ans[i], ans[i + 1] = ans[i + 1], ans[i]
        print(ans[i], end=" ")
    print()