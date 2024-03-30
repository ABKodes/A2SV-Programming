from collections import Counter
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
counts = Counter(arr)
my_dict = dict(counts)
height = max(my_dict.values())
total = len(my_dict)
print(height,total)
