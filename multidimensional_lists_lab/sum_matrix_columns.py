rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_matrix = [int(el) for el in input().split()]
    matrix.append(inner_matrix)

col_sums = []

for col in range(cols):
    col_sum = 0
    for row in range(rows):
        col_sum += matrix[row][col]
    col_sums.append(col_sum)

for c in col_sums:
    print(c)