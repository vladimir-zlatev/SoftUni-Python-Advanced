n = int(input())

matrix = []

for _ in range(n):
    inner_matrix = [int(el) for el in input().split()]
    matrix.append(inner_matrix)

diagonal = 0

for row in range(n):
    diagonal += matrix[row][row]

print(diagonal)
