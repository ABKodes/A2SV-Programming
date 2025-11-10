n, k, q = map(int, input().split())
maxTemperature = 200000
# Build frequency array using difference array technique
freq = [0] * (maxTemperature + 2)
for _ in range(n):
    l, r = map(int, input().split())
    freq[l] += 1
    freq[r + 1] -= 1
# Number of recipes recommending each temperature
current = 0
count = [0] * (maxTemperature + 1)
for i in range(1, maxTemperature + 1):
    current += freq[i]
    count[i] = current
# Admissible temperatures (where count[i] >= k)
admissible = [0] * (maxTemperature + 1)
for i in range(1, maxTemperature + 1):
    if count[i] >= k:
        admissible[i] = 1
# Prefix sum of admissible temperatures
prefix = [0] * (maxTemperature + 1)
for i in range(1, maxTemperature + 1):
    prefix[i] = prefix[i - 1] + admissible[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l - 1])
