n,m = map(int, input().split())
arr1 = [int(x) for x in input().split()]
arr2= [int(x) for x in input().split()]
arr3 = []
first= 0
second = 0
counter = 0
while first < len(arr1) or second<len(arr2):
    if second == len(arr2) or first <len(arr1) and arr2[second] > arr1[first]:
        counter +=1
        first +=1
    else:
        arr3.append(counter)
        second +=1
print(" ".join(str(x) for x in arr3))