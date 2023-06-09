text = input()

reversed_stack = list(text)

print(''.join([reversed_stack.pop() for _ in range(len(reversed_stack))]))

