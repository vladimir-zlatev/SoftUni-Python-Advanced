from collections import deque

litters = int(input())

people = deque()

while True:
    line = input()

    if line == "Start":
        break

    people.append(line)

while True:
    line = input().split()

    if line[0] == "End":
        break

    if line[0].isdigit():
        if int(line[0]) <= litters:
            print(f"{people.popleft()} got water")
            litters -= int(line[0])
        else:
            print(f"{people.popleft()} must wait")
    else:
        if line[0] == "refill":
            litters += int(line[1])

print(f"{litters} liters left")

