testCases = int(input())
for _ in range(testCases):
    n = int(input())
    candies = input()
    seen = set()
    total = 0
    for i in range(n):
        if candies[i] not in seen:
            seen.add(candies[i])
            total += 2
        else:
            total += 1
    print(total)