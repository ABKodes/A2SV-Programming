n = int(input())
decode = input()
result = []
for char in reversed(decode):
    result.insert((len(result) + 1) // 2, char)
print("".join(result[::-1]))


