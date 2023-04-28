from collections import deque

children_deque = deque()

children = input().split(" ")

toss = int(input())

for child in children:
    children_deque.append(child)

while len(children_deque) > 1:
    children_deque.rotate(-toss)
    kid = children_deque.pop()
    print(f"Removed {kid}")

last_kid = children_deque.popleft()

print(f"Last is {last_kid}")