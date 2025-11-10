n = int(input())
adjacent = {i: [] for i in range(1, n+ 1)}
totalFlipCosts = 0
for _ in range(n):
    a,b,c= map(int, input().split())
    adjacent[a].append((b, 0))
    adjacent[b].append((a, c))
    totalFlipCosts += c

costOneDirection = 0
currentCity = 1 
previousCity = -1

for _ in range(n):
    for neighbor, cost in adjacent[currentCity]:
        if neighbor != previousCity:
            costOneDirection += cost
            previousCity = currentCity
            currentCity = neighbor
            break

costOtherDirection = totalFlipCosts - costOneDirection
print(min(costOneDirection, costOtherDirection))