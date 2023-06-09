from collections import deque

kids = deque([kid for kid in input().split()])

rot = int(input())

while len(kids) > 1:
    kids.rotate(-rot)
    print(f"Removed {kids.pop()}")

print("Last is", *kids)

