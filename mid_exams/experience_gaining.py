amount_needed = int(input())
battles_count = int(input())
total_experience = 0
amount_reached = False
counter = 0

for current_battle in range(1, battles_count + 1):
    experience_gained = int(input())

    if current_battle % 3 == 0:
        experience_gained = experience_gained + (experience_gained * 0.15)
    if current_battle % 5 == 0:
        experience_gained = experience_gained - (experience_gained * 0.10)
    if current_battle % 15 == 0:
        experience_gained = experience_gained + (experience_gained * 0.05)

    counter += 1
    total_experience += experience_gained

    if total_experience >= amount_needed:
        amount_reached = True
        break

if amount_reached:
    print(f"Player successfully collected his needed experience for {counter} battles.")
else:
    result = amount_needed - total_experience
    print(f"Player was not able to collect the needed experience, {result:.2f} more needed.")