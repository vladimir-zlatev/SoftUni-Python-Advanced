clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_capacity = 0
rack_count = 0

while clothes:
    current_clothe = clothes.pop()
    current_capacity += current_clothe

    if current_capacity > rack_capacity:
        rack_count += 1
        current_capacity = 0
        clothes.append(current_clothe)
    elif current_capacity == rack_capacity:
        rack_count += 1
        current_capacity = 0
    elif current_capacity < rack_capacity and len(clothes) == 0:
        rack_count += 1


print(rack_count)