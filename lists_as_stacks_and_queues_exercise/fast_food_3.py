from collections import deque

food = int(input())

orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    current_order = orders[0]

    if current_order <= food:
        food -= current_order
        orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    print("Orders left:", ' '.join([str(x) for x in orders]))
