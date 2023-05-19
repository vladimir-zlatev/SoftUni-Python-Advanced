n = int(input())

matrix = []

for _ in range(n):
    inner_matrix = list(input())
    matrix.append(inner_matrix)

search_symbol = input()
occurrence = ()
is_break = False

for row in range(n):
    for col in range(n):
        if matrix[row][col] == search_symbol:
            occurrence = (row, col)
            is_break = True
            break
    if is_break:
        break

if occurrence:
    print(occurrence)
else:
    print(f"{search_symbol} does not occur in the matrix")