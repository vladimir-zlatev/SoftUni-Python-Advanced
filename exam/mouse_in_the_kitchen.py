from collections import deque

rows, cols = [int(x) for x in input().split(",")]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix = []
mouse_pos = []
cheeses_count = 0

for row in range(rows):
    matrix.append(list(input()))

    if 'M' in matrix[row]:
        mouse_pos = [row, matrix[row].index('M')]

    if 'C' in matrix[row]:
        cheeses_count += matrix[row].count('C')

is_outside_the_board = False
is_cheese_count_zero = False
is_trap = False
is_danger = False

while cheeses_count > 0:
    direction = input()

    if direction == "danger":
        is_danger = True
        break

    matrix[mouse_pos[0]][mouse_pos[1]] = '*'

    row = mouse_pos[0] + directions[direction][0]
    col = mouse_pos[1] + directions[direction][1]

    previous_mouse_position = [mouse_pos[0], mouse_pos[1]]

    if not (0 <= row < rows and 0 <= col < cols):
        is_outside_the_board = True
        mouse_pos = previous_mouse_position
        matrix[mouse_pos[0]][mouse_pos[1]] = 'M'
        break

    mouse_pos = [row, col]
    position = matrix[row][col]

    if position == '@':
        mouse_pos = previous_mouse_position
        matrix[mouse_pos[0]][mouse_pos[1]] = 'M'
        continue

    if position == "C":
        cheeses_count -= 1

        if cheeses_count == 0:
            matrix[row][col] = 'M'
            is_cheese_count_zero = True
            break #########
        else:
            matrix[row][col] = '*'
            #mouse_pos = matrix[row][col]

    if position == "T":
        is_trap = True
        matrix[row][col] = 'M'
        break

if is_outside_the_board:
    print("No more cheese for tonight!")

if is_cheese_count_zero:
    print("Happy mouse! All the cheese is eaten, good night!")

if is_trap:
    print("Mouse is trapped!")

if is_danger:
    print("Mouse will come back later!")

[print(''.join(r)) for r in matrix]
