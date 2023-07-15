from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milks = deque(int(x) for x in input().split(", "))
milkshakes = 0

while True:
    if milkshakes == 5:
        break

    if not chocolates:
        break

    if not cups_of_milks:
        break

    chocolate = chocolates.pop()
    if chocolate <= 0:
        continue

    cup_of_milk = cups_of_milks.popleft()
    if cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milks.append(cup_of_milk)
        chocolate -= 5
        chocolates.append(chocolate)

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print("Chocolate: ", end="")
    print(*chocolates, sep=", ")
else:
    print("Chocolate: empty")

if cups_of_milks:
    print("Milk: ", end="")
    print(*cups_of_milks, sep=", ")
else:
    print("Milk: empty")