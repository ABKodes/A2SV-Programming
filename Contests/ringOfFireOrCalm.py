from collections import deque

n, m = map(int, input().split())
roads = []
for i in range(m):
    u, v = map(int, input().split())
    roads.append((min(u, v), max(u, v), i))

conflictGraph = {i: [] for i in range(m)}
for i in range(m):
    for j in range(i + 1, m):
        u1, v1, _ = roads[i]
        u2, v2, _ = roads[j]
        if (u1 < u2 and u2 < v1 and v1 < v2) or \
           (u2 < u1 and u1 < v2 and v2 < v1):
            conflictGraph[i].append(j)
            conflictGraph[j].append(i)

colors = [-1] * m
resultChars = [''] * m

possible = True
for i in range(m):
    if colors[i] == -1:
        q = deque()
        q.append((i,0))
        colors[i] = 0
        
        while q:
            currentRoadIndex, currentColor = q.popleft()
            originalIndex = roads[currentRoadIndex][2]
            resultChars[originalIndex] = 'i' if currentColor == 0 else 'o'
            
            for neighborRoadIndex in conflictGraph[currentRoadIndex]:
                if colors[neighborRoadIndex] == -1:
                    colors[neighborRoadIndex] = 1 - currentColor
                    q.append((neighborRoadIndex, 1 - currentColor))
                elif colors[neighborRoadIndex] == currentColor:
                    possible = False
                    break
            if not possible:
                break
        if not possible:
            break

if possible:
    print(''.join(resultChars))
else:
    print('Impossible')