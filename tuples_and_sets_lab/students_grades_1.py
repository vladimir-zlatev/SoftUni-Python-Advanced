number = int(input())

students = {}

for _ in range(number):
    name, grade = tuple(input().split())

    grade = float(grade)

    if name in students:
        students[name].append(grade)
    else:
        students[name] = [grade]

for key, value in students.items():
    print(f"{key} -> {' '.join(f'{x:.2f}' for x in value)} (avg: {(sum(value) / len(value)):.2f})")