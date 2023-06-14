status_of_pirate_ship = list(map(int, input().split('>')))
status_of_the_warship = list(map(int, input().split('>')))
maximum_health_capacity = int(input())
ships_not_survived = False

command = input()

while command != 'Retire':
    command = command.split()
    action = command[0]

    if action == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(status_of_the_warship):
            status_of_the_warship[index] -= damage
            if status_of_the_warship[index] <= 0:
                ships_not_survived = True
                print(f"You won! The enemy ship has sunken.")

    elif action == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index in range(len(status_of_pirate_ship)) and end_index in range(len(status_of_pirate_ship)):
            for current_index in range(start_index, end_index + 1):
                status_of_pirate_ship[current_index] -= damage
                if status_of_pirate_ship[current_index] <= 0:
                    ships_not_survived = True
                    print(f"You lost! The pirate ship has sunken.")
                    break

    elif action == 'Repair':
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(str(status_of_pirate_ship)):
            if health <= maximum_health_capacity:
                status_of_pirate_ship[index] += health
            else:
                status_of_pirate_ship[index] = maximum_health_capacity

    elif action == 'Status':
        count = [int(section) for section in status_of_pirate_ship if section < maximum_health_capacity * 0.2]
        number_of_sections_to_be_repaired = len(count)
        print(f"{number_of_sections_to_be_repaired} sections need repair.")

    command = input()

if not ships_not_survived:
    pirate_ship_sum = sum(int(section) for section in status_of_pirate_ship)
    war_ship_sum = sum(int(section) for section in status_of_the_warship)
    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {war_ship_sum}")


