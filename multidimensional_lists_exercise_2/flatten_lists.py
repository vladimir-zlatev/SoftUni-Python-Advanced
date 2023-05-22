matrix = [[x for x in x.split()] for x in input().split("|")]

for row in range(len(matrix)):
    [print(x, end=" ") for x in matrix.pop()]