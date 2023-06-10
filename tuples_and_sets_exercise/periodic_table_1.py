number = int(input())

elements = set()

for _ in range(number):
    elem = input().split()
    for el in elem:
        elements.add(el)

print(*elements, sep="\n")