from collections import deque

wasted = 0

cups_deque = deque([int(c) for c in input().split()])
bottle_deque = deque([int(b) for b in input().split()])

while cups_deque and bottle_deque:
    cup = cups_deque.popleft()
    bottle = bottle_deque.pop()

    if bottle > cup:
        wasted += bottle - cup
    elif bottle < cup:
        cup = cup - bottle
        cups_deque.appendleft(cup)

if bottle_deque:
    print(f"Bottles: {' '.join([str(b) for b in bottle_deque])}")

if cups_deque:
    print(f"Cups: {' '.join([str(c) for c in cups_deque])}")

print(f"Wasted litters of water: {wasted}")
