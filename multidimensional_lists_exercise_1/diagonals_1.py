n = int(input())

matrix = []

for _ in range(n):
    inner_list = [int(x) for x in input().split(', ')]
    matrix.append(inner_list)

primary_diagonal = []
secondary_diagonal = []

for row in range(n):
    primary_diagonal.append(matrix[row][row])

row = 0
for col in range(n-1, -1, -1):
    secondary_diagonal.append(matrix[row][col])
    row += 1

print(f"Primary diagonal: " + ', '.join([str(x) for x in primary_diagonal]) + f". Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: " + ', '.join([str(x) for x in secondary_diagonal]) + f". Sum: {sum(secondary_diagonal)}")