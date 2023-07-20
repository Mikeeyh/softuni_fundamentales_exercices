force_sides = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")
        if force_user not in [user for users in force_sides.values() for user in users]:
            if force_side not in force_sides:
                force_sides[force_side] = []
            force_sides[force_side].append(force_user)

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        for current_side, users in force_sides.items():
            if force_user in users:
                users.remove(force_user)
                break

        if force_side not in force_sides:
            force_sides[force_side] = []
        force_sides[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for side, users in force_sides.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
