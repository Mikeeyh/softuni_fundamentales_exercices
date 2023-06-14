treasure_chest = input().split("|")
command = input()
gain = 0
average_gain = 0

while command != "Yohoho!":
    command_data = command.split()
    action = command_data[0]

    if action == "Loot":
        items = command_data[1:]
        for item in items:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif action == "Drop":
        index = int(command_data[1])
        if 0 <= index < len(treasure_chest):
            item = treasure_chest.pop(index)
            treasure_chest.append(item)

    elif action == "Steal":
        count = int(command_data[1])
        stolen_items = treasure_chest[-count:]
        treasure_chest = treasure_chest[:-count]
        print(", ".join(stolen_items))

    command = input()

for treasure_item in treasure_chest:
    gain += len(treasure_item)
item_count = len(treasure_chest)

if not gain == 0 and not item_count == 0:
    average_gain = gain / item_count

if not len(treasure_chest) == 0:
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

# OR ----------------------------------------------------------

treasure_chest = input().split("|")
command = input()

while command != "Yohoho!":
    command_data = command.split()
    action = command_data[0]

    if action == "Loot":
        items = command_data[1:]
        for item in items:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif action == "Drop":
        index = int(command_data[1])
        if 0 <= index < len(treasure_chest):
            item = treasure_chest.pop(index)
            treasure_chest.append(item)

    elif action == "Steal":
        count = int(command_data[1])
        stolen_items = treasure_chest[-count:]
        treasure_chest = treasure_chest[:-count]
        print(", ".join(stolen_items))

    command = input()

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    total_length = sum(len(item) for item in treasure_chest)
    average_gain = total_length / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
