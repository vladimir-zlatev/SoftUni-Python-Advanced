from collections import deque

parentheses = deque()

text = input()
is_balanced = True

for par in text:
    if par == "(" or par == "{" or par == "[":
        parentheses.append(par)
    elif par in {"]", ")", "}"} and len(parentheses) == 0:
        is_balanced = False
        break
    elif parentheses:
        if par == "]" and parentheses[-1] == "[" or par == "}" and parentheses[-1] == "{" or par == ")" and parentheses[-1] == "(":
            parentheses.pop()
        else:
            is_balanced = False
            break
    else:
        is_balanced = False
        break

if is_balanced and len(parentheses) == 0:
    print("YES")
else:
    print("NO")