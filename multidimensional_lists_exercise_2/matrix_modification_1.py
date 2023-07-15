n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]


while True:
    command, *info = input().split()

    if command == "END":
        break

    row, col, value = [int(x) for x in info]

    if not (0 <= row < n and 0 <= col < n):
        print("Invalid coordinates")
    elif command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value

[print(*r) for r in matrix]