numbers = list(map(int, input().split()))
command = input()

while command != 'Finish':
    command = command.split()
    action = command[0]

    if action == "Add":
        value = int(command[1])
        numbers.append(value)

    elif action == "Remove":
        value = int(command[1])
        if value in numbers:
            numbers.remove(value)

    elif action == "Replace":
        value = int(command[1])
        replacement = int(command[2])
        if value in numbers:
            index = numbers.index(value)
            numbers.pop(index)
            numbers.insert(index, replacement)

    elif action == "Collapse":
        value = int(command[1])
        numbers = [num for num in numbers if not num < value]

    command = input()

print(*numbers, sep=" ")
