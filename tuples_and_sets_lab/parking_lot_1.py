number = int(input())

parking = set()

for _ in range(number):
    direction, reg_number = input().split(", ")

    if direction == "IN":
        parking.add(reg_number)
    elif direction == "OUT":
        if reg_number in parking:
            parking.remove(reg_number)

if parking:
    print(*parking, sep="\n")
else:
    print("Parking Lot is Empty")