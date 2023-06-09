from collections import deque

water = int(input())

people = deque()

command = input()

while command != "Start":
    people.append(command)

    command = input()

com = input()
while com != "End":
    instruction = com.split()

    if instruction[0].isdigit():
        liters = int(instruction[0])
        person = people.popleft()
        if liters <= water:
            water -= liters
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    elif instruction[0] == "refill":
        water += int(instruction[1])

    com = input()

print(f"{water} liters left")
