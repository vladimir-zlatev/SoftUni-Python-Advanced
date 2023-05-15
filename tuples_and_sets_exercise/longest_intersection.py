n = int(input())

longest_intersection = set()
for _ in range(n):
    first, second = input().split("-")
    first_set = set([f for f in range(int(first.split(",")[0]), int(first.split(",")[1]) + 1)])
    second_set = set([s for s in range(int(second.split(",")[0]), int(second.split(",")[1]) + 1)])

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")
