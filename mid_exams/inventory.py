items = input().split(', ')
command = input()

while command != 'Craft!':
    command = command.split(' - ')
    action = command[0]
    item = command[1]

    if action == 'Collect':
        if item not in items:
            items.append(item)
    elif action == 'Drop':
        if item in items:
            index = items.index(item)
            items.pop(index) # we can do it without searching for the index and using pop / we can use remove
    elif action == 'Combine Items':
        item = item.split(':')
        old_item = item[0]
        new_item = item[1]
        if old_item in items:
            index = items.index(old_item)
            items.insert(index + 1, new_item)

    elif action == 'Renew':
        if item in items:
            items.remove(item)
            items.append(item)

    command = input()

print(', '.join(items))

# OR --------------------------------------------------------

journal = input().split(", ")
command = input()

while command != "Craft!":
    command_data = command.split(" - ")
    action = command_data[0]
    item = command_data[1]

    if action == "Collect":
        if item not in journal:
            journal.append(item)
    elif action == "Drop":
        if item in journal:
            journal.remove(item)
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in journal:
            index = journal.index(old_item)
            journal.insert(index + 1, new_item)
    elif action == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)

    command = input()

print(", ".join(journal))
