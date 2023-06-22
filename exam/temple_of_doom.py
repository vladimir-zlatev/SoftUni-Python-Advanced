from collections import deque

tools = deque([int(t) for t in input().split()])
substances = deque([int(s) for s in input().split()])
challenges = deque([int(c) for c in input().split()])

while tools and substances and challenges:
    if not challenges:
        break

    tool = tools.popleft()
    substance = substances.pop()

    check = tool * substance

    if check in challenges:
        challenges.remove(check)
    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance > 0:
            substances.append(substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(t) for t in tools)}")
if substances:
    print(f"Substances: {', '.join(str(sub) for sub in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(cha) for cha in challenges)}")
