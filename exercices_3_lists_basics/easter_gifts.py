gifts = input().split()
gifts_list = []
command = input()

while command != "No Money":
    command = command.split()
    action = command[0]
    gift = command[1]
    if action == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = "None"

    elif action == "Required":
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif action == "JustInCase":
        gifts[-1] = gift

    command = input()

# result = ' '.join([gift for gift in gifts if gift != "None"])
# print(result)

# OR

for current_gift in gifts:
    if current_gift != "None":
        gifts_list.append(current_gift)
print(' '.join(gifts_list))


