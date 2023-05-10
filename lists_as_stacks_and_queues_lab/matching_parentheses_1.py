text = input()

expression = list(text)

parentheses_stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        parentheses_stack.append(index)
    elif expression[index] == ")":
        start_index = parentheses_stack.pop()
        end_index = index + 1
        print("".join(expression[start_index:end_index]))


