s = input()
n = len(s)
t = [] 
u = []
smallestCharacterIndex = [None] * n
smallestCharacterIndex[-1] = s[-1]
for i in range(n-2, -1, -1):
    smallestCharacterIndex[i] = min(smallestCharacterIndex[i+1], s[i])
for i in range(n):
    t.append(s[i])
    while t and (i == n-1 or t[-1] <= smallestCharacterIndex[i+1]):
        u.append(t.pop())
print("".join(u))