# There is exactly one segment (a continuous block of numbers) in the array where:
#
#     - All the numbers in the segment are equal.
#
#     - This segment is either:
#
#         - At the start of the array, OR
#
#         - At the end of the array, OR
#
#         - Surrounded by numbers that are greater than the segment’s value.
#
#     If there are zero or more than one such segments, the canyon is not a true canyon.


def is_true_canyon(n, a):
    valid_segments = 0
    i = 0
    while i < n:
        start = i
        current = a[i]
        # Extend the segment as long as elements are equal
        while i < n and a[i] == current:
            i += 1
        end = i - 1
        # Check if the segment is valid
        valid = True
        if start > 0 and a[start - 1] <= current:
            valid = False
        if end < n - 1 and a[end + 1] <= current:
            valid = False
        if valid:
            valid_segments += 1
    # Check if there is exactly one valid segment
    return "YES" if valid_segments == 1 else "NO"

testCases = int(input())
for _ in range(testCases):
    n = int(input())  
    a = list(map(int, input().split()))  
    print(is_true_canyon(n, a))  