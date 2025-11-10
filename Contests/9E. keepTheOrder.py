n = int(input())
enter = list(map(int, input().split()))
exit = list(map(int, input().split()))

exitPosition = {troop: index for index, troop in enumerate(exit)}
fired  = 0
maxExitPosition = -1
for troop in enter:
    if exitPosition[troop] < maxExitPosition:
        fired += 1
    else:
        maxExitPosition = exitPosition[troop]
print(fired)