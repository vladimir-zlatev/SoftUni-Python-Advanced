rows, cols = [int(x) for x in input().split(", ")]

matrix = []
sub_matrix = []

max_sum = float('-inf')

for _ in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    matrix.append(inner_list)

for row in range(rows - 1):
    for col in range(cols - 1):
        first_row = [matrix[row][col], matrix[row][col+1]]
        second_row = [matrix[row+1][col], matrix[row+1][col+1]]
        current_sum = sum(first_row) + sum(second_row)
        if max_sum < current_sum: #
            max_sum = current_sum
            sub_matrix = [first_row, second_row]

for row in range(2):
    print(*sub_matrix[row], sep=' ')

print(max_sum)
