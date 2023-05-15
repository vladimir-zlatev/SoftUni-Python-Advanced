n = int(input())

parking = set()

for _ in range(n):
    direction, reg_number = input().split(', ')
    if direction == "IN":
        parking.add(reg_number)
    else:
        if reg_number in parking:
            parking.remove(reg_number)

if parking:
    print(*parking, sep='\n')
else:
    print("Parking Lot is Empty")