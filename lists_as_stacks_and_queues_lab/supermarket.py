from collections import deque

customer_deque = deque()

while True:
    line = input()

    if line == "End":
        break

    if line == "Paid":
        while customer_deque:
            print(customer_deque.popleft())
    else:
        customer_deque.append(line)

print(f"{len(customer_deque)} people remaining.")
