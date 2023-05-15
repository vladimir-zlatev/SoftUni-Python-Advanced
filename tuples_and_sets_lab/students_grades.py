n = int(input())

students = {}

for _ in range(n):
    name, grade = tuple(input().split())
    grade = float(grade)

    if name in students:
        students[name].append(grade)
    else:
        students[name] = [grade]

for s_name, grades in students.items():
    print(f"{s_name} -> {' '.join([str(f'{gr:.2f}') for gr in grades])} (avg: {sum(grades)/len(grades):.2f})")

