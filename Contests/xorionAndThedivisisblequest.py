from math import gcd

n = int(input().strip())
nums = []
while len(nums) < n:
    nums.extend(map(int, input().split()))

totalGcd = 0
for x in nums:
    totalGcd = gcd(totalGcd, x)

answerFound = False
for x in nums:
    if totalGcd % x == 0:
        print(x)
        answerFound = True
        break

if not answerFound:
    print(-1)