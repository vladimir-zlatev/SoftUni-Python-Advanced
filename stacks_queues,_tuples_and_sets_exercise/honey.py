from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(x for x in input().split())

honey = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        operator = symbols.popleft()
        if operator == "+":
            honey += abs(current_bee + current_nectar)
        elif operator == "-":
            honey += abs(current_bee - current_nectar)
        elif operator == "*":
            honey += abs(current_bee * current_nectar)
        elif operator == "/":
            if current_nectar == 0:
                continue
            else:
                honey += abs(current_bee / current_nectar)

    elif current_nectar <= current_bee:
        bees.appendleft(current_bee)

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: ", end="")
    print(*bees, sep=", ")

if nectar:
    print(f"Nectar left: ", end="")
    print(*nectar, sep=", ")