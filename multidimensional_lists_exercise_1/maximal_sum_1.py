rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sub_matrix = []

max_sum = float('-inf')

for row in range(rows-2):
    for col in range(cols -2):
        first = [matrix[row][col], matrix[row][col+1], matrix[row][col+2]]
        second = [matrix[row+1][col], matrix[row+1][col + 1], matrix[row+1][col + 2]]
        third = [matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]

        current_sum = sum(first) + sum(second) + sum(third)

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [first, second, third]

print(f"Sum = {max_sum}")
[print(*row) for row in sub_matrix]