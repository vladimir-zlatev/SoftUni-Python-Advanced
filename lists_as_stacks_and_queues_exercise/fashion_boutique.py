clothes_stack = [int(x) for x in input().split(" ")]

capacity = int(input())

racks = 1

current_capacity = capacity
while clothes_stack:
    cloth = clothes_stack.pop()

    if cloth <= current_capacity:
        current_capacity -= cloth
    else:
        current_capacity = capacity - cloth
        racks += 1

print(racks)