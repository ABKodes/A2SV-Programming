t = int(input())  
for _ in range(t):  
    n, k, q = map(int, input().split())  
    a = list(map(int, input().split()))  
    
    current_run = 0  
    left = 0
    total = 0
        for right in range(n):
            if a[right] > q:
                left = right + 1  # Reset window
            else:
                window_size = right - left + 1
                if window_size >= k:
                    total += window_size - k + 1
        print(total)