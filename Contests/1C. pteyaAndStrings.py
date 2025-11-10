str1 = input()
str2 = input()
n = len(str1)
if str1.lower() == str2.lower():
    print(0)
else:
    for i in range(n):
        if str1[i].lower() < str2[i].lower():
            print(-1)
            break
        elif str1[i].lower() > str2[i].lower():
            print(1)
            break