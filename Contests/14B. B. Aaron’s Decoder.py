
t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    component1_ones = 0  
    component2_ones = 0  
    for k in range(n):
        if k % 2 == 0:  
            if a[k] == '1':
                component1_ones += 1
            if b[k] == '1':
                component2_ones += 1
        else:  
            if a[k] == '1':
                component2_ones += 1
            if b[k] == '1':
                component1_ones += 1

    b_positions_in_comp1 = n // 2

    b_positions_in_comp2 = (n + 1) // 2 
    
    possible1 = component1_ones <= b_positions_in_comp1
    possible2 = component2_ones <= b_positions_in_comp2

    if possible1 and possible2:
        print("YES")
    else:
        print("NO")

