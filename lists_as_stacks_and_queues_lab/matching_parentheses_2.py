# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

text = input()

parentheses = []

for idx in range(len(text)):
    if text[idx] == "(":
        parentheses.append(idx)
    elif text[idx] == ")":
        if parentheses:
            first_index = parentheses.pop()
            last_index = idx + 1

            print(text[first_index:last_index])


