reverse_number_stack = input().split(" ")

for idx in range(len(reverse_number_stack)):
    print(reverse_number_stack.pop(), end=" ")