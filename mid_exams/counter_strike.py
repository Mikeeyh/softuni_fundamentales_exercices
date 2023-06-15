initial_energy = int(input())
command = input()
battle_won = 0
not_success = False

while command != 'End of battle':
    energy_needed = int(command)

    if energy_needed <= initial_energy:
        battle_won += 1
        initial_energy -= energy_needed
        if battle_won % 3 == 0:
            initial_energy += battle_won
    else:
        print(f"Not enough energy! Game ends with {battle_won} won battles and {initial_energy} energy")
        not_success = True
        break

    command = input()

if not not_success:
    print(f"Won battles: {battle_won}. Energy left: {initial_energy}")
