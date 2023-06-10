from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())

wasted = 0

while bottles:
    bottle = bottles.pop()
    cup = cups.popleft()

    if bottle > cup:
        wasted += bottle - cup
    elif bottle < cup:
        cup = cup - bottle
        cups.appendleft(cup)

    if not cups:
        break

if not cups:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")

if not bottles:
    print(f"Cups: {' '.join([str(x) for x in cups])}")

print(f"Wasted litters of water: {wasted}")