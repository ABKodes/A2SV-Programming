testCases = int(input())
for _ in range(testCases):
    n,k  = map(int, input().split())
    arr = list(map(int, input().split()))
    MOD = 10**9 + 7
    initial = sum(arr) % MOD
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    maxSubarraySum = float("-inf")
    minPrefix = 0
    for i in range(1, n + 1):
        current = prefix[i] - minPrefix
        if current > maxSubarraySum:
            maxSubarraySum = current
        if prefix[i] < minPrefix:
            minPrefix = prefix[i]
    if maxSubarraySum <= 0:
        print(initial % MOD)
        continue
    power = pow(2, k, MOD)
    totalAddedPower = (power - 1) % MOD
    totalAddedPower = (totalAddedPower * maxSubarraySum) % MOD
    totalPower = (totalAddedPower + initial) % MOD
    print(totalPower)