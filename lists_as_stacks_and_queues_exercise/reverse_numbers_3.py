from collections import deque

reverse_number_stack = input().split(" ")
for rns in range(len(reverse_number_stack)):
    print(reverse_number_stack.pop(), end=" ")