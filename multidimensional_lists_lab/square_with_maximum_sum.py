import math

rows, cols = [int(el) for el in input().split(", ")]

matrix = []

max_sum = - math.inf
max_matrix = []

for _ in range(rows):
    inner_matrix = [int(el) for el in input().split(", ")]
    matrix.append(inner_matrix)

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        bellow_element = matrix[row_index + 1][col_index]
        diagonal = matrix[row_index + 1][col_index + 1]

        current_sum = current_element + next_element + bellow_element + diagonal

        if max_sum < current_sum:
            max_sum = current_sum
            max_matrix = [[current_element, next_element], [bellow_element, diagonal]]

print(*max_matrix[0])
print(*max_matrix[1])
print(max_sum)


