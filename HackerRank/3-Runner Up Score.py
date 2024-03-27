if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    result.sort()
    result.pop()
    print(result[-1])
            