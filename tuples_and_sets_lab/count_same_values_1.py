numbers = tuple(float(x) for x in input().split())

numbers_dict = {}

for el in numbers:
    if el in numbers_dict:
        numbers_dict[el] += 1
    else:
        numbers_dict[el] = 1


for key, value in numbers_dict.items():
    print(f"{key:.1f} - {value} times")