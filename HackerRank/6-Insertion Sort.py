#!/bin/python3


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    last = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] > last:
            arr[i+1] = arr[i]
            print(" ".join(map(str, arr)))
        else:
            arr[i+1] = last
            print(" ".join(map(str, arr)))
            break
    else:
        arr[0] = last
        print(" ".join(map(str, arr)))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
