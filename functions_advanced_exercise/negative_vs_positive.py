def print_positive_negative(positive, negative):
    print(negative)
    print(positive)
    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]

negative_numbers = sum([x for x in numbers if x < 0])
positive_numbers = sum([x for x in numbers if x > 0])

print_positive_negative(positive_numbers, negative_numbers)

