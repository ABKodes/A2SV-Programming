testCases = int(input())
for _ in range(testCases):
    n, k = map(int, input().split())
    s = input().strip()
    score = 0

    # Step 1: Calculate current score
    for i in range(n):
        if s[i] == 'W':
            score += 1
            if i > 0 and s[i-1] == 'W':
                score += 1

    # Special case: no wins at all
    if score == 0:
        print(max(0, 2 * k - 1))
        continue

    # Step 2: Find gaps of Ls between Ws
    first = s.find('W')
    last = s.rfind('W')
    gaps = []
    i = first
    while i <= last:
        if s[i] == 'L':
            start = i
            while i <= last and s[i] == 'L':
                i += 1
            gaps.append(i - start)
        else:
            i += 1

    # Step 3: Fill gaps (smallest first)
    gaps.sort()
    for gap in gaps:
        if k >= gap:
            score += 2 * gap + 1  # +2 per flip, +1 for bridging
            k -= gap
        else:
            score += 2 * k
            k = 0
            break

    # Step 4: Use remaining flips on outside Ls
    leading = s[:first].count('L')
    trailing = s[last+1:].count('L')
    remaining_flips = min(k, leading + trailing)
    score += 2 * remaining_flips

    print(score)