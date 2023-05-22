size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

bombs = [[int(y) for y in x.split(",")] for x in input().split()]

for bomb in bombs:
    row, col = bomb

    bomb_value = matrix[row][col]

    if bomb_value >= 0:

        row_start = row - 1 if 0 < row else 0
        row_end = row + 1 if row < size - 1 else row
        col_start = col - 1 if 0 < col else 0
        col_end = col + 1 if col < size - 1 else col

        for r in range(row_start, row_end + 1):
            for c in range(col_start, col_end + 1):
                if matrix[r][c] > 0:
                    matrix[r][c] = matrix[r][c] - bomb_value

active_cells = []
for r in range(size):
    for c in range(size):
        if matrix[r][c] > 0:
            active_cells.append(matrix[r][c])

print(f"Alive cells: {len(active_cells)}")
print(f"Sum: {sum(active_cells)}")
[print(*row) for row in matrix]

