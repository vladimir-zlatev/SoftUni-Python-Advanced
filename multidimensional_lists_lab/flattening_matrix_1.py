rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    [matrix.append(x) for x in inner_list]

print(matrix)