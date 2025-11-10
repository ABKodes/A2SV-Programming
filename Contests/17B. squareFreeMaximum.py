import math

def isSquareFree(num):
    if num < 0:
        return True
    if num == 0:
        return False
    integerSquareRoot = math.isqrt(num)
    return integerSquareRoot * integerSquareRoot != num

n = int(input())
arr = list(map(int, input().split()))
result = -float('inf')

for num in arr:
    if isSquareFree(num):
        if num > result:
            result = num
            
print(result)
