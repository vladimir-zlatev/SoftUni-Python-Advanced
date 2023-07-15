from collections import deque
size = int(input())

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

position = []

matrix = []

hazelnuts = 0

instructions = deque(input().split(", "))

is_trap = False
is_outside = False

for row in range(size):
    matrix.append(list(input()))
    if "s" in matrix[row]:
        position = [row, matrix[row].index("s")]
        matrix[row][position[1]] = '*'

while True:
    if hazelnuts == 3:
        break

    for inst in instructions:
        pos_row = moves[inst][0] + position[0]
        pos_col = moves[inst][1] + position[1]

        if not (0 <= pos_row < size and 0 <= pos_col <= size):
            is_outside = True
            break

        current_position = matrix[pos_row][pos_col]

        position = [pos_row, pos_col]

        if current_position == "h":
            hazelnuts += 1
            matrix[pos_row][pos_col] = "*"
        elif current_position == "t":
            is_trap = True
            break

    break

if hazelnuts == 3:
    print("Good job! You have collected all hazelnuts!")
elif is_outside:
    print("The squirrel is out of the field.")
elif is_trap:
    print("Unfortunately, the squirrel stepped on a trap...")
from collections import deque
size = int(input())

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

position = []

matrix = []

hazelnuts = 0

instructions = deque(input().split(", "))

is_trap = False
is_outside = False

for row in range(size):
    matrix.append(list(input()))
    if "s" in matrix[row]:
        position = [row, matrix[row].index("s")]
        matrix[row][position[1]] = '*'

while True:
    if hazelnuts == 3:
        break

    for inst in instructions:
        pos_row = moves[inst][0] + position[0]
        pos_col = moves[inst][1] + position[1]

        if not (0 <= pos_row < size and 0 <= pos_col <= size):
            is_outside = True
            break

        current_position = matrix[pos_row][pos_col]

        position = [pos_row, pos_col]

        if current_position == "h":
            hazelnuts += 1
            matrix[pos_row][pos_col] = "*"
        elif current_position == "t":
            is_trap = True
            break

    break

if hazelnuts == 3:
    print("Good job! You have collected all hazelnuts!")
elif is_outside:
    print("The squirrel is out of the field.")
elif is_trap:
    print("Unfortunately, the squirrel stepped on a trap...")
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")




print(f"Hazelnuts collected: {hazelnuts}")


