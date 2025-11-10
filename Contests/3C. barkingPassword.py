password = input()
n = int(input())
temp = []
for _ in range(n):
    temp.append(input())
exact = first = second = False
for word in temp:
    if password in temp:
        exact = True
    if password[0] == word[1]:
        first = True
    if password[1] == word[0]:
        second = True
if exact or (first and second):
    print("YES")
else:
    print("NO")