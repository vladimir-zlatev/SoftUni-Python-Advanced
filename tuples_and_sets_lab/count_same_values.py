numbers = tuple([float(x) for x in input().split()])

result = {}

for el in numbers:
    if el in result:
        result[el] += 1
    else:
        result[el] = 1

for num, times in result.items():
    print(f"{num:.1f} - {times} times")