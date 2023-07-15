from collections import deque

task_times = deque([int(x) for x in input().split()])
number_of_tasks = deque([int(x) for x in input().split()])

ducky_type = {
    'Darth Vader Ducky': (0, 60),
    'Thor Ducky': (61, 120),
    'Big Blue Rubber Ducky': (121, 180),
    'Small Yellow Rubber Ducky': (181, 240),
}

ducky_count = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0,
}

while task_times and number_of_tasks:
    time = task_times.popleft()
    task = number_of_tasks.pop()

    calculation = task * time

    if ducky_type['Darth Vader Ducky'][0] <= calculation <= ducky_type['Darth Vader Ducky'][1]:
        ducky_count['Darth Vader Ducky'] += 1
    elif ducky_type['Thor Ducky'][0] <= calculation <= ducky_type['Thor Ducky'][1]:
        ducky_count['Thor Ducky'] += 1
    elif ducky_type['Big Blue Rubber Ducky'][0] <= calculation <= ducky_type['Big Blue Rubber Ducky'][1]:
        ducky_count['Big Blue Rubber Ducky'] += 1
    elif ducky_type['Small Yellow Rubber Ducky'][0] <= calculation <= ducky_type['Small Yellow Rubber Ducky'][1]:
        ducky_count['Small Yellow Rubber Ducky'] += 1
    elif ducky_type['Small Yellow Rubber Ducky'][1] < calculation:
        task -= 2
        number_of_tasks.append(task)
        task_times.append(time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in ducky_count.items():
    print(f"{key}: {value}")