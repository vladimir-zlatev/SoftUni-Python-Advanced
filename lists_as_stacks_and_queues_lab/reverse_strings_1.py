text = input()

string_stack = list(text)

for el in range(len(string_stack)):
    reversed_element = string_stack.pop()
    print(reversed_element, end="")
