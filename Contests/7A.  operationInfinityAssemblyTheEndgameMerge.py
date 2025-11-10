testCases= int(input())
for _ in range(testCases):
    n, m, k= list(map(int, input().split()))
    a= input()
    b= input()
    a= ''.join(sorted([c for c in a]))
    b= ''.join(sorted([c for c in b]))
    c=""
    i,j=0,0
    count_a=0
    count_b=0
    while i<n and j<m:
        if ord(a[i])<ord(b[j]):
            count_b=0
            if count_a<k:
                c+=a[i]
                count_a+=1
                i+=1
            else:
                c+=b[j]
                count_a=0
                j+=1
        else:
            count_a=0
            if count_b<k:
                c+=b[j]
                count_b+=1
                j+=1
            else:
                c+=a[i]
                count_b=0
                i+=1
    print(c)