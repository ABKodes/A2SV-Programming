n = int(input())
res = list(map(int, input().split()))
temp = []
for index, number in enumerate(res):
    temp.append((number, index + 1))
temp.sort()
left,right = 0, len(temp) - 1
while left < right:
    print(temp[left][1], temp[right][1])
    left += 1
    right -= 1
