number = int(input())

longest_intersection = list()

for _ in range(number):
    intersec = input().split("-")
    first_start, first_end = [int(x) for x in intersec[0].split(",")]
    second_start, second_end = [int(x) for x in intersec[1].split(",")]

    first_range = set(x for x in range(first_start, first_end + 1))
    second_range = set(x for x in range(second_start, second_end + 1))

    current_intersec = first_range.intersection(second_range)

    if len(current_intersec) > len(longest_intersection):
        longest_intersection = list(current_intersec.copy())

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")