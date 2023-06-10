guests = set()

number = int(input())

for _ in range(number):
    guest = input()

    if guest not in guests:
        guests.add(guest)

guest_came_to_party = input()
while guest_came_to_party != "END":

    if guest_came_to_party in guests:
        guests.remove(guest_came_to_party)

    guest_came_to_party = input()

print(len(guests))

print(*sorted(guests), sep="\n")
