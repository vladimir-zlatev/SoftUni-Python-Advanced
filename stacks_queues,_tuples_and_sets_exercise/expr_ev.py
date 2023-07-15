from collections import deque

numbers = deque(input().split())

result = deque()

for _ in range(len(numbers)):

    ch = numbers.popleft()

    calculation = 0

    if ch == "*":
        calculation = int(result.popleft())
        for _ in range(len(result)):
            calculation *= int(result.popleft())
        result.appendleft(calculation)
    elif ch == "/":
        calculation = int(result.popleft())
        for _ in range(len(result)):
            calculation //= int(result.popleft())
        result.appendleft(calculation)
    elif ch == "+":
        calculation = int(result.popleft())
        for _ in range(len(result)):
            calculation += int(result.popleft())
        result.appendleft(calculation)
    elif ch == "-":
        calculation = int(result.popleft())
        for _ in range(len(result)):
            calculation -= int(result.popleft())
        result.appendleft(calculation)
    else:
        result.append(ch)

print(*result)
