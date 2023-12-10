from collections import deque

number = int(input())
distance_deque = deque()

for _ in range(number):
    petrol, distance = [int(x) for x in input().split()]

    distance_deque.append([petrol, distance])

initial_petrol = 0
initial_distance = 0

for idx in range(len(distance_deque)):
    is_break = False
    working_deque = distance_deque.copy()
    while working_deque:
        current_petrol, current_distance = working_deque.popleft()

        initial_petrol += current_petrol
        initial_distance += current_distance

        if initial_petrol < initial_distance:
            distance_deque.rotate(-1)
            is_break = True
            initial_distance = 0
            initial_petrol = 0
            break

    if not is_break:
        print(idx)
        break
