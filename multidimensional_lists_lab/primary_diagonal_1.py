rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split()]
    matrix.append(inner_list)

sum_prime_diagonal = 0

for row in range(rows):
    sum_prime_diagonal += matrix[row][row]

print(sum_prime_diagonal)
