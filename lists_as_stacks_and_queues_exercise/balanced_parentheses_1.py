from collections import deque

parentheses = deque()

sequence = input()

is_break = False

for seq in sequence:
    if seq in ("(", "[", "{"):
        parentheses.append(seq)
    else:
        if not parentheses:
            print("NO")
            break
        else:
            last = parentheses.pop()

            if (seq == ")" and last != "(") or \
                    (seq == "}" and last != "{") or \
                    (seq == "]" and last != "["):
                print("NO")
                break
else:
    if parentheses:
        print("NO")
    else:
        print('YES')