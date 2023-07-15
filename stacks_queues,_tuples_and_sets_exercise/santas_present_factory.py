from collections import deque

materials = deque(int(x) for x in input().split())
magics = deque(int(x) for x in input().split())

toys = deque()
toys_magic = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}


while materials and magics:
    is_toy = False

    material = materials.pop()
    if material == 0:
        continue

    magic = magics.popleft()
    if magic == 0:
        materials.append(material)
        continue

    magic_level = material * magic

    for key, value in toys_magic.items():
        if value == magic_level:
            toys.append(key)
            is_toy = True
            continue

    if magic_level < 0 and not is_toy:
        magic_level = material + magic
        materials.append(magic_level)
    elif magic_level > 0 and not is_toy:
        material += 15
        materials.append(material)

if {"Doll", "Wooden train"}.issubset(toys) or {"Teddy bear", "Bicycle"}.issubset(toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magics:
    print(f"Magic left: {', '.join([str(x) for x in magics])}")

[print(x + ":", toys.count(x)) for x in sorted(set(toys))]