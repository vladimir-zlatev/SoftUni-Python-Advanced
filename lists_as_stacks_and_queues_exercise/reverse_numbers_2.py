stack_numbers = list(int(x) for x in input().split())

for x in range(len(stack_numbers)):
    print(stack_numbers.pop(), end=" ")

