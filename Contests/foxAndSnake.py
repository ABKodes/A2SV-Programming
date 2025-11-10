row, column = map(int, input().split())
snake = []
for i in range(row):
    if i % 2 == 0:
        snake.append(["#"] * column)
    else:
        if (i // 2) % 2 == 0:
            snake.append(["."] * (column - 1) + ["#"])
        else:
            snake.append(["#"] + ["."] * (column - 1))
for row in snake:
    print("".join(row))