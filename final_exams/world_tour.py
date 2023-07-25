stops = input()

while True:
    command = input()

    if command == 'Travel':
        break

    command_data = command.split(':')
    action = command_data[0]

    if action == 'Add Stop':
        index = int(command_data[1])
        given_string = command_data[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + given_string + stops[index:]
        print(stops)

    elif action == 'Remove Stop':
        start_index = int(command_data[1])
        end_index = int(command_data[2])
        if 0 <= start_index < len(stops):
            if start_index <= end_index < len(stops):
                stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)

    elif action == 'Switch':
        old_string = command_data[1]
        new_string = command_data[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

print(f'Ready for world tour! Planned stops: {stops}')

# OR -----------------------------------------------------------------

def add_stop(stops, index, string):
    if 0 <= index < len(stops):
        stops = stops[:index] + string + stops[index:]
    return stops

def remove_stop(stops, start_index, end_index):
    if 0 <= start_index <= end_index < len(stops):
        stops = stops[:start_index] + stops[end_index+1:]
    return stops

def switch_string(stops, old_string, new_string):
    if old_string in stops:
        stops = stops.replace(old_string, new_string)
    return stops

stops = input()

while True:
    command = input()
    if command == "Travel":
        break

    command_data = command.split(":")
    action = command_data[0]

    if action == "Add Stop":
        index = int(command_data[1])
        string = command_data[2]
        stops = add_stop(stops, index, string)
        print(stops)

    elif action == "Remove Stop":
        start_index = int(command_data[1])
        end_index = int(command_data[2])
        stops = remove_stop(stops, start_index, end_index)
        print(stops)

    elif action == "Switch":
        old_string = command_data[1]
        new_string = command_data[2]
        stops = switch_string(stops, old_string, new_string)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
