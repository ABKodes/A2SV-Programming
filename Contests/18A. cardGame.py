t = int(input())
for _ in range(t):
    n, k1, k2 = map(int, input().split())
    player1 = list(map(int, input().split()))
    player2 = list(map(int, input().split()))
    if n in player1:
        print("YES")
    else:
        print("NO")