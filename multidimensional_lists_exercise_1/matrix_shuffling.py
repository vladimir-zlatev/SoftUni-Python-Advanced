def check_values(info):
    return {info[0], info[2]}.issubset(row_range) and {info[1], info[3]}.issubset(col_range)


def check_command(command, info):
    if command == "swap" and check_values(info) and len(info) == 4:
        row1, col1, row2, col2 = info

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(r) for r in matrix], sep="\n")
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]


row_range = range(rows)
col_range = range(cols)

while True:
    command_type, *info_list = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == "END":
        break

    check_command(command_type, info_list)0