from collections import deque

people_deque = deque()

liters = int(input())

is_break = False

while True:
    line = input()

    if line == "End":
        break

    if line == "Start":
        while True:
            command = input()

            if command == "End":
                is_break = True
                break

            if command.isdigit():
                current_liters = int(command)
                person_name = people_deque.popleft()
                if current_liters <= liters:
                    liters -= current_liters
                    print(f"{person_name} got water")
                else:
                    print(f"{person_name} must wait")
            else:
                refill_liters = int(command.split(" ")[1])
                liters += refill_liters
    else:
        people_deque.append(line)

    if is_break:
        break

print(f"{liters} liters left")

