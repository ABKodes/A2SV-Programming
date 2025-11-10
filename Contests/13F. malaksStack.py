m = int(input())

# Store operations
operations = [None] * (m + 1)  # 1-based indexing
positions = [0] * (m + 1)  # When each operation is remembered

# Read input
for i in range(m):
    parts = list(map(int, input().split()))
    p = parts[0]
    t = parts[1]
    if t == 1:
        x = parts[2]
        operations[p] = ("push", x)
    else:
        operations[p] = ("pop", None)
    positions[p] = i

# Process operations in remembrance order
current_stack = []  # Stack of values
results = []

for i in range(m):
    # Find the operation remembered at step i
    for p in range(1, m + 1):
        if positions[p] == i:
            idx = p
            break
    
    # Rebuild stack up to the current remembered operations in original order
    current_stack = []
    for j in range(1, m + 1):
        if positions[j] <= i:  # Operation j is remembered (positions[j] <= i)
            op, val = operations[j]
            if op == "push":
                current_stack.append(val)
            elif current_stack:
                current_stack.pop()
    
    # Store the top element
    results.append(current_stack[-1] if current_stack else -1)

# Print results
for result in results:
    print(result)