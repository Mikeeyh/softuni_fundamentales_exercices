while True:
    command = input()
    new_string = ''

    if command == 'End':
        break

    if command == 'SoftUni':
        continue

    for index in range(len(command)):
        current_index = command[index] * 2
        new_string += current_index

    print(new_string)



