targets = list(map(int, input().split()))
command = input()

while command != 'End':
    command = command.split()
    action = command[0]

    if action == 'Shoot':
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif action == 'Add':
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")

    elif action == 'Strike':
        index = int(command[1])
        radius = int(command[2])
        start_index = index - radius
        end_index = index + radius
        if start_index >= 0 and end_index < len(targets):
            del targets[start_index:end_index+1]
        else:
            print("Strike missed!")

    command = input()

print(*targets, sep="|")

# OR ------------------------------------------------------------------

targets = list(map(int, input().split()))
command = input()

while command != 'End':
    command = command.split()
    action = command[0]

    if action == 'Shoot':
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif action == 'Add':
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")

    elif action == 'Strike':
        index = int(command[1])
        radius = int(command[2])
        if index - radius in range(len(targets)) and index + radius in range(len(targets)):
            start_index = index - radius
            end_index = index + radius

            for index in range(end_index, start_index -1, -1):
                targets.pop(index)
        else:
            print("Strike missed!")

    command = input()

print(*targets, sep="|")
