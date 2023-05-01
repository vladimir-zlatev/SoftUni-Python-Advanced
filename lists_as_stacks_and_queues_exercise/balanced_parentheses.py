from collections import deque

parentheses = list()

line = list(input())

is_balanced = True

if len(parentheses) % 2 != 0:
    print("NO")
else:
    for element in line:
        if element == "(" or element == "[" or element == "{":
            parentheses.append(element)
        else:
            if parentheses:
                left_element = parentheses.pop()
                if left_element == "(" and element != ")":
                    is_balanced = False
                    break
                if left_element == "{" and element != "}":
                    is_balanced = False
                    break
                if left_element == "[" and element != "]":
                    is_balanced = False
                    break
            else:
                is_balanced = False
                break

    if is_balanced:
        print("YES")
    else:
        print("NO")
