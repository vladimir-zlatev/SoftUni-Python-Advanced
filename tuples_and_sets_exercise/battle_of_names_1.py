n = int(input())

even_sum = set()
odd_sum = set()

for i in range(1, n + 1):
    text = input()

    sum_name = sum([ord(ch) for ch in text]) // i

    if sum_name % 2 == 0:
        even_sum.add(sum_name)
    else:
        odd_sum.add(sum_name)

if sum(even_sum) == sum(odd_sum):
    print(', '.join(str(x) for x in odd_sum.union(even_sum)))
elif sum(odd_sum) > sum(even_sum):
    print(', '.join(str(x) for x in odd_sum.difference(even_sum)))
elif sum(even_sum) > sum(odd_sum):
    print(', '.join(str(x) for x in odd_sum.symmetric_difference(even_sum)))