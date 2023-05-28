def grocery_store(**kwargs):
    result = []
    result_str = ""

    for product, quantity in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        result.append((product, quantity))

    for x in result:
        result_str += f"{x[0]}: {x[1]}\n"
    return result_str


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
