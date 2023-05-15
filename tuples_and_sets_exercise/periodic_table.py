n = int(input())

periodic_table = set()

for _ in range(n):
    [periodic_table.add(ele) for ele in input().split()]

print(*periodic_table, sep='\n')