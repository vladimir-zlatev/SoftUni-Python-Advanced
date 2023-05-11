from collections import deque

n = int(input())

numbers = deque()

for _ in range(n):
    line = input().split()

    if line[0] == "1":
        numbers.append(int(line[1]))
    elif line[0] == "2":
        if numbers:
            numbers.pop()
    elif line[0] == "3":
        if numbers:
            print(max(numbers))
    elif line[0] == "4":
        if numbers:
            print(min(numbers))

numbers.reverse()
print(", ".join([str(x) for x in numbers]))

