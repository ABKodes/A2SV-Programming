testCases = int(input())
for _ in range(testCases):
    n = int(input())
    paint = input()
    first, last = paint.find("B"), paint.rfind("B")
    print(last - first + 1)
    