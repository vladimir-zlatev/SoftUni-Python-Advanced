def check_values(values):
    row, col = values[0], values[1]
    return {row}.issubset(row_range) and {col}.issubset(col_range)


n = int(input())

row_range = set(range(n))
col_range = set(range(n))

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    if check_values(info):
        row, col, value = info
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")


[print(*row) for row in matrix]