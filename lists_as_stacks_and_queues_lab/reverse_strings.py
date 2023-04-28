text = input()

text_stack = list(text)

for _ in range(len(text_stack)):
    print(text_stack.pop(), end="")

