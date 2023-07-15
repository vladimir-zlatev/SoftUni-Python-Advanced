position = {
    'up' : (-1, 0),
    'down' : (1, 0),
    'left' : (0, -1),
    'right': (0, 1)
}

size = int(input())

matrix = [list(input().split()) for _ in range(size)]
#matrix = [[el for el in input().split(" ")] for r in range(size)]

max_path = []
max_eggs = 0
direction = None

while True:

    for row in range(size):
        for col in range(size):

            if matrix[row][col] == "B":
                for direc, pos in position.items():
                    eggs = 0
                    path = []
                    current_direction = ''

                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    while 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "X":
                            break

                        eggs += int(matrix[pos_row][pos_col])
                        path.append([pos_row, pos_col])

                        pos_row = pos_row + pos[0]
                        pos_col = pos_col + pos[1]

                    if eggs > max_eggs:
                        max_eggs = eggs
                        max_path = path
                        direction = direc

    break

print(direction)
[print(el) for el in max_path]
print(max_eggs)
