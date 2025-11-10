testCount = int(input().strip())

for _ in range(testCount):
    n, k = map(int, input().split())
    maxPeaks = (n - 1) // 2
    if k > maxPeaks:
        print(-1)
        continue

    permArray = list(range(1, n + 1))
    indexPos = 1  # 0-based index corresponding to position 2
    remainingPeaks = k

    while remainingPeaks > 0 and indexPos + 1 < n:
        permArray[indexPos], permArray[indexPos + 1] = permArray[indexPos + 1], permArray[indexPos]
        indexPos += 2
        remainingPeaks -= 1

    print(*permArray)