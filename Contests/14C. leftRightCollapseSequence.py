
from collections import deque

    
    


# Read the number of test cases
t = int(input())
# Process each test case
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input().strip()

    dequeForward = deque(a)
    removedElements = []
    for i in range(n): 
        command = s[i]
        if command == 'L':
            if dequeForward:
                 removedElements.append(dequeForward.popleft())
        else: 
            if dequeForward:
                removedElements.append(dequeForward.pop())

    results = [0] * n 
    dequeReverse = deque() 
    currentProduct = 1 

    for k in range(n - 1, -1, -1):
        command = s[k]
        element_to_add = removedElements[k]

        if command == 'L':
            
            dequeReverse.appendleft(element_to_add)
            
            currentProduct = (currentProduct * element_to_add) % m
        else:
            dequeReverse.append(element_to_add)
            
            currentProduct = (currentProduct * element_to_add) % m

        results[k] = currentProduct

    print(*(results))
