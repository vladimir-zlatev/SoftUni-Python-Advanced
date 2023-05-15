n = int(input())

even_set = set()
odd_set = set()

for idx in range(1, n + 1):
    name = input()

    sum_ = sum(ord(x) for x in name) // idx

    if sum_ % 2 == 0:
        even_set.add(sum_)
    else:
        odd_set.add(sum_)

if sum(odd_set) == sum(even_set):
    union = odd_set.union(even_set)
    print(*union, sep=", ")
elif sum(odd_set) > sum(even_set):
    difference = odd_set.difference(even_set)
    print(*difference, sep=", ")
elif sum(even_set) > sum(odd_set):
    symmetric_difference = odd_set.symmetric_difference(even_set)
    print(*symmetric_difference, sep=", ")

