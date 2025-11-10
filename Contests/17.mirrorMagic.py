for _ in range(int(input())):
    a = input()
    b = ""
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 'p':
            b += 'q'
        elif a[i] == 'q':
            b += 'p'
        else:
            b += a[i]
    print(b)