# 1 2 3 |4 5 6 | 7 88          7 88 4 5 6 1 2 3

matrix = input().split("|")

sub_list = []

for line in matrix[::-1]:
    sub_list.extend(line.split())

print(*sub_list)