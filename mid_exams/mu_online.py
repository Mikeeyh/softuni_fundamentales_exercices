dungeon_rooms = input().split('|')
initial_health = 100
initial_bitcoins = 0
room_count = 0
monster_success = False

for room in dungeon_rooms:
    room_count += 1
    current_room = room.split()
    command = current_room[0]
    number = int(current_room[1])

    if command == 'potion':
        if initial_health + number > 100:
            print(f'You healed for {100 - initial_health} hp.')
            initial_health += 100 - initial_health
        else:
            initial_health += number
            print(f'You healed for {number} hp.')
        print(f"Current health: {initial_health} hp.")

    elif command == 'chest':
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        initial_health -= number
        if not initial_health <= 0:
            print(f"You slayed {command}.")
        else:
            monster_success = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_count}")
            break

if not monster_success:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
