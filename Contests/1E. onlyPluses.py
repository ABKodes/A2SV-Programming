testCases = int(input())
for _ in range(testCases):
    a,b,c = map(int, input().split())
    nums = [a,b,c]
    for _ in range(5):
        nums.sort()
        if nums[0] < 10:
            nums[0] += 1
        else:
            break
    product = nums[0] * nums[1] * nums[2]
    print(product)