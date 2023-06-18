command = input()
message_list = []
messages = []

while command != 'end':
    command = command.split()
    action = command[0]

    if action == "Chat":
        message = command[1]
        message_list.append(message)

    elif action == "Delete":
        message = command[1]
        if message in message_list:
            message_list.remove(message)

    elif action == "Edit":
        message = command[1]
        new_message = command[2]
        if message in message_list:
            index = message_list.index(message)
            message_list.pop(index)
            message_list.insert(index, new_message)

    elif action == "Pin":
        message = command[1]
        if message in message_list:
            index = message_list.index(message)
            message_list.pop(index)
            message_list.append(message)

    elif action == "Spam":
        spam_messages = command[1:]
        message_list.extend(spam_messages)

    command = input()

result = [word for word in message_list]
print('\n'.join(result))

