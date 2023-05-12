from collections import deque

food = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders[0]

    if current_order > food:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break
    else:
        food -= orders.popleft()
else:
    print("Orders complete")

