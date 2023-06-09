from collections import deque

supermarket_deque = deque()

people = input()

while people != "End":
    if people == "Paid":
        for _ in range(len(supermarket_deque)):
            print(supermarket_deque.popleft())
    else:
        supermarket_deque.append(people)

    people = input()

print(f"{len(supermarket_deque)} people remaining.")
