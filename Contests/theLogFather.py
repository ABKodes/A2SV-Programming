MOD = 10 ** 9 + 7
powers = {}
for y in range(2, 61):
    curr = y
    p_list = []
    while curr <= 10 ** 18:
        p_list.append(curr)
        if curr > 10 ** 18 // y:
            break
        curr *= y
    powers[y] = p_list

def sumGUpToX(X):
    if X < 4:
        return 0
    totalSum = 0
    maxYForX = X.bit_length() - 1
    for y in range(2, maxYForX + 1):
        ySegmentStart = max(4, 1 << y)
        ySegmentEnd = min(X, (1 << (y + 1)) - 1)
        if ySegmentStart > ySegmentEnd:
            continue
        p_list = powers[y]
        for z, power in enumerate(p_list, 1):  # z starts at 1
            nextPower = (p_list[z] if z < len(p_list) else 10 ** 18 + 1)
            segStart = max(ySegmentStart, power)
            segEnd = min(ySegmentEnd, nextPower - 1)
            if segStart <= segEnd:
                count = segEnd - segStart + 1
                totalSum = (totalSum + z * count) % MOD
    return totalSum

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    ans = (sumGUpToX(r) - sumGUpToX(l - 1) + MOD) % MOD
    print(ans)
