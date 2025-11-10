from collections import defaultdict
import sys

input = sys.stdin.read
data = input().split()

MOD = 1000000007


def solve(n, a):
    s = set(a)
    bad_total = 0

    for x in s:
        pre = [0] * (n + 1)
        b = [0] * n
        for i in range(n):
            b[i] = -1 if a[i] > x else 1
            pre[i + 1] = pre[i] + b[i]

        count = defaultdict(int)
        _sum = 0
        j = 0
        check = False

        for i in range(n):
            if a[i] == x:
                if not check:
                    count[0] = 1
                check = True
                while j < i:
                    count[pre[j + 1]] += 1
                    j += 1
            _sum += count[pre[i + 1]]
        bad_total += _sum

    total = n * (n + 1) // 2
    print(total - bad_total)


def main():
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx : idx + n]))
        idx += n
        solve(n, a)


if __name__ == "__main__":
    main()