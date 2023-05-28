def concatenate(*args, **kwargs):
    result = ""
    for x in args:
        result += x

    for key, value in kwargs.items():
        if key in result:
            result = result.replace(str(key), str(value))

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))