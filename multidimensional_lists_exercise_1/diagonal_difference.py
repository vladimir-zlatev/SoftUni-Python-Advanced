n = int(input())

matrix = [[int(el) for el in input().split()] for r in range(n)]

primary_diagonal = sum([matrix[r][r] for r in range(n)])
secondary_diagonal = sum([matrix[r][n - r - 1] for r in range(n)])

print(abs(primary_diagonal - secondary_diagonal))