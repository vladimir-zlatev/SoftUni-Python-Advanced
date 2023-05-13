from collections import deque

clothes_deque = deque([int(x) for x in input().split()])

rack_size = int(input())

racks = 0
clothes = 0

while clothes_deque:
    clothe = clothes_deque.pop()

    clothes += clothe

    if clothes > rack_size:
        racks += 1
        clothes = 0
        clothes_deque.append(clothe)
    elif clothes == rack_size:
        racks += 1
        clothes = 0
    elif clothes < rack_size and len(clothes_deque) == 0:
        racks += 1

print(racks)
