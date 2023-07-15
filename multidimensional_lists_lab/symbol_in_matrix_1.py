n = int(input())

matrix = []

for _ in range(n):
    inner_list = list(input())
    matrix.append(inner_list)

symbol = input()

is_break = False

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            is_break = True
            break
    if is_break:
        break

if not is_break:
    print(f"{symbol} does not occur in the matrix")