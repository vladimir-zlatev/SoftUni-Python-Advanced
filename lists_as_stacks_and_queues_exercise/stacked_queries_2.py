stacked_queries = []

n = int(input())

for _ in range(n):
    command = input().split()
    instruction = command[0]

    if instruction == '1':
        stacked_queries.append(int(command[1]))
    elif instruction == '2':
        if stacked_queries:
            stacked_queries.pop()
    elif instruction == '3':
        if stacked_queries:
            print(max(stacked_queries))
    elif instruction == '4':
        if stacked_queries:
            print(min(stacked_queries))

print(', '.join([str(stacked_queries.pop()) for _ in range(len(stacked_queries))]))
