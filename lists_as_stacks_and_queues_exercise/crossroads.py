from collections import deque

green_line = int(input())
free_window = int(input())

cars = deque()

passed = 0
is_break = False

while True:
    command = input()

    if command == "END":
        break

    if command != "green":
        cars.append(command)

    if command == "green":
        current_line = green_line
        current_window = free_window
        while len(cars) > 0:
            car = cars.popleft()

            if len(car) < current_line:
                passed += 1
                current_line -= len(car)

            elif len(car) <= current_line + free_window:
                passed += 1
                break

            elif len(car) >= current_line + free_window:
                print("A crash happened!")
                print(f"{car} was hit at {car[current_line + free_window]}.")
                is_break = True
                break

    if is_break:
        break

if not is_break:
    print("Everyone is safe.")
    print(f"{passed} total cars passed the crossroads.")



