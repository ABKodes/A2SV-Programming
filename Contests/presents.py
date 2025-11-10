n = int(input())
present = list(map(int, input().split()))
answer = [0] * n
for i in range(n):
    answer[present[i]-1] = i+1
print(answer)