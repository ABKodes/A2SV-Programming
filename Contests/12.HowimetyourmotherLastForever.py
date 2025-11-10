n = int(input())
count = {"z": 0, "e": 0, "r": 0, "o": 0, "n": 0}
strs = input()
result = []
for i in strs:
    if i in count:
        count[i] += 1
maxOnes = min(count["o"], count["n"], count["e"])
count["o"] -= maxOnes
count["n"] -= maxOnes
count["e"] -= maxOnes
maxZeros = min(count["z"], count["e"], count["r"], count["o"])
for i in range(maxOnes):
    result.append(1)
for i in range(maxZeros):
    result.append(0)
print(" ".join(map(str, result)))
