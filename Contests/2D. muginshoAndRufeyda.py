n, t = map(int, input().split())
result = -1
for i in range(10 ** (n-1), 10 ** (n)):
    if i % t == 0:
        result = i
        break
print(result)