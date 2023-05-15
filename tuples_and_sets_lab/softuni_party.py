n = int(input())

reservation = set()

for _ in range(n):
    reservation.add(input())

guests = set()

while True:
    guest = input()

    if guest == "END":
        break

    guests.add(guest)

not_receive_guests = reservation.difference(guests)

print(len(not_receive_guests))
for g in sorted(not_receive_guests):
    print(g)