from collections import deque

numbers = deque([int(x) for x in input().split()])

numbers.reverse()

print(*numbers, sep=" ")