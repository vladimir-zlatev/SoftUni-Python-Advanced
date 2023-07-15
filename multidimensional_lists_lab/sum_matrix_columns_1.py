rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    inner_list = [int(x) for x in input().split()]
    matrix.append(inner_list)

for col in range(cols):
    col_sum = 0
    for row in range(rows):
        col_sum += matrix[row][col]

    print(col_sum)
