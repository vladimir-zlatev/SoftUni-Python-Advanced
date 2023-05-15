n, m = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for _ in range(n):
    first_set.add(input())

for _ in range(m):
    second_set.add(input())

intersection = first_set.intersection(second_set)

print(*intersection, sep='\n')