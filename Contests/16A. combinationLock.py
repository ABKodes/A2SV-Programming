n = int(input())
initial = input()
target = input()

totalMoves = 0
for i in range(n):
    initialDigit = int(initial[i])
    targetDigit = int(target[i])
    
    clockwiseMoves = (initialDigit - targetDigit) % 10
    
    counterClockwiseMoves = (targetDigit - initialDigit) % 10
    
    totalMoves += min(clockwiseMoves, counterClockwiseMoves)
    
print(totalMoves)
    
