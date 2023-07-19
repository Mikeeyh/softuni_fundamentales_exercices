force_side_dict = {}

counter_1 = 0
counter_2 = 0

command = input()

while command != "Lumpawaroo":
    if "|" in command:
        command = command.split(" | ")
        force_side, force_user = command

        if force_side not in force_side_dict.keys():
            force_side_dict[force_side] = []

        if force_user not in force_side_dict.values():
            if force_user not in force_side_dict[force_side]:
                force_side_dict[force_side].append(force_user)
                counter_1 += 1

    elif "->" in command:
        command = command.split(" -> ")
        force_side, force_user = command

        if force_side not in force_side_dict.keys():
            force_side_dict[force_side] = []

        if force_user not in force_side_dict.values():
            if force_user not in force_side_dict[force_side]:
                force_side_dict[force_side].append(force_user)
                counter_2 += 1

    command = input()

for key, value in force_side_dict.items():
    print(f"Side:{key}, Members: {counter_1}")
    for name in value:
        print(f"! {name}")
