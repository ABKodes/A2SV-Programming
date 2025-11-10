testCases = int(input())
for _ in range(testCases):
    n, k = map(int, input().split())
    color = input()
    # The three possible patterns to match 
    patterns = ["RGB", "GBR", "BRG"]
    minimumChanges = float('inf')
    # Checking for the first k characters
    for pattern in patterns:
        changes = 0
        for i in range(k):
            expected = pattern[i % 3]
            if color[i] != expected:
                changes += 1
        
        minimumChanges = min(minimumChanges, changes)
        # Slide the window across the string (positions k upto n)
        for i in range(k, n):
            # handling a new character entering the window
            expected = pattern[i % 3]
            if color[i] != expected:
                changes += 1
            # handling a character leaving the window
            expected = pattern[(i - k) % 3]
            if color[i - k] != expected:
                changes -= 1
            minimumChanges = min(minimumChanges, changes)
    print(minimumChanges)