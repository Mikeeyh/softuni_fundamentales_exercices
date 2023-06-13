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
            items.pop(index)
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
