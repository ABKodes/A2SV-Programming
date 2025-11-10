testCases = int(input())
for _ in range(testCases):
    n = int(input())
    if n != 2:
        nums = list(range(1, n * n + 1))
        matrix = [[0] * n for _ in range(n)]
        index = 0
        for i in range(n):
            for j in range(n):
                if (i + j) % 2 == 0 and index < len(nums):
                    matrix[i][j] = nums[index]
                    index += 1
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0 and index < len(nums):
                    matrix[i][j] = nums[index]
                    index += 1
    else:
        print(-1)
        continue
    for row in matrix:
        print(*row)