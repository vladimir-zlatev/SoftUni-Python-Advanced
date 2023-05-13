from collections import deque

petrol_distance_deque = deque()

petrol_pumps = int(input())

for _ in range(petrol_pumps):
    petrol_distance_deque.append(input().split())

for index in range(petrol_pumps):
    tank = 0
    failed = False

    for current in petrol_distance_deque:
        tank += int(current[0])

        if tank < int(current[1]):
            petrol_distance_deque.append(petrol_distance_deque.popleft())
            break
        else:
            tank -= int(current[1])
    else:
        print(index)
        break



