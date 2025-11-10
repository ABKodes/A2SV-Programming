line = input()
if line[0].islower():
    print(line[0].upper() + line[1:])
else:
    print(line)