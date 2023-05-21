from collections import deque

rows, cols = [int(x) for x in input().split()]

word = list(input())

current_word = deque(word)

for row in range(rows):

    while len(current_word) < cols:
        current_word.extend(word)

    if row % 2 == 0:
        print(''.join([current_word.popleft() for col in range(cols)]))
    else:
        print(''.join([current_word.popleft() for col in range(cols)][::-1]))
