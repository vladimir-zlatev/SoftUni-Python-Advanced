from collections import deque

food = int(input())

orders = deque([int(x) for x in input().split(" ")])

if orders:
    print(max(orders))

is_break = False

while orders:
    current_order = orders.popleft()

    if current_order > food:
        is_break = True
        print(f"Orders left: {current_order}", end=" ")
        break

    food -= current_order

if is_break:
    for o in orders:
        print(o, end=" ")
else:
    print("Orders complete")
