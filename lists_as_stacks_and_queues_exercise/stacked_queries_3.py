stacked_queries = []

n = int(input())

for _ in range(n):
    line = input().split()

    command = line[0]

    if command == '1':
        stacked_queries.append(int(line[1]))
    elif command == '2':
        if stacked_queries:
            stacked_queries.pop()
    elif command == '3':
        if stacked_queries:
            print(max(stacked_queries))
    elif command == '4':
        if stacked_queries:
            print(min(stacked_queries))

# stacked_queries.reverse()
# print(", ".join(str(sq) for sq in stacked_queries))

print(", ".join([str(stacked_queries.pop()) for _ in range(len(stacked_queries))]))