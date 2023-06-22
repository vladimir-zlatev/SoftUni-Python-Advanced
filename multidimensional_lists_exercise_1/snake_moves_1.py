from collections import deque

rows, cols = [int(x) for x in input().split()]

text = input()

matrix = []

snake = deque(text)

for row in range(rows):
    if row % 2 == 0:
        while len(snake) < cols:

            for x in text:
                snake.append(x)

        inner_row = []
        for x in range(cols):
            inner_row.append(snake.popleft())
        matrix.append(inner_row)
    else:
        while len(snake) < cols:

            for x in text:
                snake.append(x)

        inner_row = []
        for x in range(cols):
            inner_row.append(snake.popleft())
        matrix.append(inner_row[::-1])

print(*[''.join(r) for r in matrix], sep='\n')
