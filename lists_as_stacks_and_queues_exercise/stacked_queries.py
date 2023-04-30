stack_queries = []

n = int(input())

for _ in range(n):
    line = input().split(" ")

    if line[0] == "1":
        stack_queries.append(int(line[1]))
    elif line[0] == "2" and stack_queries:
        stack_queries.pop()
    elif line[0] == "3" and stack_queries:
        print(max(stack_queries))
    elif line[0] == "4" and stack_queries:
        print(min(stack_queries))

# result = []
#
# for _ in range(len(stack_queries)):
#     result.append(str(stack_queries.pop()))
#
# print(", ".join(result))

while stack_queries:
    element = stack_queries.pop()
    if stack_queries:
        print(element, end=", ")
    else:
        print(element)