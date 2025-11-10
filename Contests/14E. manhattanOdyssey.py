from typing import List, Tuple

C = 1000

def main():
    # Read input
    n = int(input())
    points: List[Tuple[Tuple[int, int], int]] = []
    
    # Read points and process
    for i in range(n):
        x, y = map(int, input().split())
        points.append(((x // C, y), i))
    
    # Sort points based on custom criteria
    points.sort(key=lambda p: (p[0][0], 
                             p[0][1] if p[0][0] % 2 == 0 else -p[0][1]))
    
    # Print indices (1-based)
    print(' '.join(str(p[1] + 1) for p in points))

if __name__ == "__main__":
    main()