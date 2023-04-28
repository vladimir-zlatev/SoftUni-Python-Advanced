text = input()

text_list = list(text)

parentheses_stack = []

for idx in range(len(text_list)):
    if text_list[idx] == "(":
        parentheses_stack.append(idx)

    if text_list[idx] == ")":
        first_index = parentheses_stack.pop()
        last_index = idx + 1
        print("".join(text_list[first_index:last_index:]))
