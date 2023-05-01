from collections import deque

n = int(input())

petrol_distance = deque()

for _ in range(n):
    petrol_distance.append([int(x) for x in input().split()])

for i in range(n):
    fuel = 0
    failed = False

    for current_fuel, current_distance in petrol_distance:
        fuel += current_fuel

        if current_distance > fuel:
            failed = True
            break
        else:
            fuel -= current_distance

    if failed:
        petrol_distance.append(petrol_distance.popleft())
    else:
        print(i)
        break


