routes = input().split('||')
amount_of_fuel = int(input())
amount_of_ammunition = int(input())
command = []

for element in routes:

    if element == 'Titan':
        print(f"You have reached Titan, all passengers are safe.")
        break

    command = element.split()
    type_of_command = command[0]

    if type_of_command == 'Travel':
        number = int(command[1])
        amount_of_fuel -= number
        print(f"The spaceship travelled {number} light-years.")

    elif type_of_command == 'Enemy':
        enemy_armour = int(command[1])
        if amount_of_ammunition >= enemy_armour:
            amount_of_ammunition -= enemy_armour
            print(f"An enemy with {enemy_armour} armour is defeated.")
        else:
            fuel_needed_to_escape = 2 * enemy_armour
            if fuel_needed_to_escape > amount_of_fuel:
                print('Mission failed!')
                break
            else:
                amount_of_fuel -= fuel_needed_to_escape
                print(f"An enemy with {enemy_armour} is outmaneuvered.")

    elif type_of_command == 'Repair':
        number_of_ammunition_and_fuel_added = int(command[1])
        amount_of_fuel += number_of_ammunition_and_fuel_added
        amount_of_ammunition += 2 * number_of_ammunition_and_fuel_added
        print(f"Ammunitions added: {number_of_ammunition_and_fuel_added * 2}.")
        print(f"Fuel added: {number_of_ammunition_and_fuel_added}.")

