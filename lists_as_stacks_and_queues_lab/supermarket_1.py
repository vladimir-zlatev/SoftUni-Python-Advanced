from collections import deque

customer_queue = deque()

while True:
    line = input()

    if line == "End":
        break

    if line == "Paid":
        while customer_queue:
            customer = customer_queue.popleft()
            print(customer)
    else:
        customer_queue.append(line)

print(f"{len(customer_queue)} people remaining.")