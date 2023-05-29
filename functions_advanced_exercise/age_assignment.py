def age_assignment(*args, **kwargs):
    result = {}
    result_str = ""

    for arg in args:
        result[arg] = ""

    for name in result:
        for key, value in kwargs.items():
            if str(name).startswith(key):
                result[name] = value

    result = sorted(result.items(), key=lambda x: x[0])

    for x in result:
        result_str += f"{x[0]} is {x[1]} years old.\n"

    return result_str


print(age_assignment("Peter", "George", G=26, P=19))