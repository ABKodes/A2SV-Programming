from typing import Counter

testCases = int(input())
for _ in range(testCases):
    a,b,c = map(int, input().split())
    solution = [a,b,c]
    result = 0
    if Counter(solution)[0] < 2:
        result += 1
    print(result)