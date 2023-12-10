from collections import deque

quantity_food = int(input())

orders = deque(int(x) for x in input().split())

if orders:
    print(max(orders))

while orders:
    next_order = orders.popleft()

    if quantity_food >= next_order:
        quantity_food -= next_order
        continue
    else:
        orders.appendleft(next_order)
        break

if orders:
    print(f"Orders left:", ' '.join(str(order) for order in orders))
else:
    print("Orders complete")

