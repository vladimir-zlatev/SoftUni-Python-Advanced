rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

bombs = [[int(y) for y in x.split(",")] for x in input().split()]

for bomb in bombs:
    row, col = bomb

    row_start = row - 1 if row > 0 else 0
    row_end = 1


    print(row, col)


print(matrix)

print(bombs)

