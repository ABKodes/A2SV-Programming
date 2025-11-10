# SOlve the codeforces question Mostly Red but mostly blue
# https://codeforces.com/problemset/problem/1709/A
# The problem is to find the minimum number of operations required to make all elements in the array equal to 1 or 0.
# The operations allowed are to change an element from 1 to 0 or from 0 to 1.
# The input consists of an integer n followed by n integers representing the array.
# The output is the minimum number of operations required.
# The solution uses a greedy approach to find the minimum number of operations required.
# The algorithm works as follows:
# 1. Read the input values.
# 2. Sort the array in descending order.
# 3. Initialize redSum and blueSum to 0 and the sum of the array respectively.
# 4. Initialize redCount and blueCount to 0 and n respectively.
# 5. Iterate through the array and update redSum, blueSum, redCount, and blueCount.
# 6. If redCount < blueCount and redSum > blueSum, print "YES" and break the loop.
# 7. If the loop completes without finding a solution, print "NO".

testCases = int(input())
for _ in range(testCases):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    redSum, blueSum = 0, sum(arr)
    redCount, blueCount = 0, n

    for i in range(n):
        redSum += arr[i]
        blueSum -= arr[i]
        redCount += 1
        blueCount -= 1

        if redCount < blueCount and redSum > blueSum:
            print("YES")
            break
    else:
        print("NO")
        