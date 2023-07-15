from collections import deque

healing_dict = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100,
}

healing_result = {}

textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    current_value = textile + medicament

    if current_value in healing_dict.values():
        key = {i for i in healing_dict if healing_dict[i] == current_value}
        val = list(key)[0]

        if val not in healing_result:
            healing_result[val] = 0

        healing_result[val] += 1
    elif current_value > healing_dict['MedKit']:
        if 'MedKit' not in healing_result:
            healing_result['MedKit'] = 0

        healing_result['MedKit'] += 1

        difference = current_value - healing_dict['MedKit']
        element = medicaments.pop() + difference
        medicaments.append(element)
    else:
        medicament += 10
        medicaments.append(medicament)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_healing = sorted(healing_result.items(), key=lambda x: (-x[1], x[0]))

for key, value in sorted_healing:
    print(f"{key} - {value}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")



