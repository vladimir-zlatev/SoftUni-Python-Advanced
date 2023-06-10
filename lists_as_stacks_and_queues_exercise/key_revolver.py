from collections import deque

bullet_price = int(input())
size_gun_barrel = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
intelligence_value = int(input())
count = 0

while bullets:
    bullet = bullets.pop()
    lock = locks.popleft()
    count += 1

    if bullet > lock:
        locks.appendleft(lock)
        print("Ping!")
    else:
        print("Bang!")

    if not bullets:
        break

    if count % size_gun_barrel == 0:
        print("Reloading!")

    if not locks:
        break




earned = intelligence_value - count * bullet_price

if len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${earned}")