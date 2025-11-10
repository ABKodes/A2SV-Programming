def bounty_dilemma(cases):
    res = []
    for c in cases:
        if '<' in c and '>' in c:
            res.append('?')
        elif '<' in c:
            res.append('<')
        elif '>' in c:
            res.append('>')
        elif '=' in c:
            res.append('=')

    return res


# input
n = int(input())
cases = []
for _ in range(n):
    c = input()
    cases.append(c)
# print(cases)

# call func
answers = bounty_dilemma(cases)
for i in range(n):
    print(answers[i])