string = input()
command = input()

while True:
    if command == "Reveal":
        print(f"You have a new text message: {string}")
        break

    command_data = command.split(":|:")
    action = command_data[0]

    if action == "InsertSpace":
        index = int(command_data[1])
        string = string[:index] + " " + string[index:]
        print(string)

    elif action == "Reverse":
        substring = command_data[1]
        if substring in string:
            string = string.replace(substring, "", 1)  # deleting the first occurrence only
            string = string + substring[::-1]
            print(string)
        else:
            print('error')

    elif action == "ChangeAll":
        substring = command_data[1]
        replacement = command_data[2]
        string = string.replace(substring, replacement)
        print(string)
    command = input()

# OR -------------------------------------------------

def decrypting_message(message):

    while True:
        command = input()

        if command.startswith("Reveal"):
            print(f"You have a new text message: {message}")
            break

        elif command.startswith("InsertSpace"):
            current_command, index = command.split(":|:")
            message = message[:int(index)] + " " + message[int(index):]
            print(message)

        elif command.startswith("Reverse"):
            current_command, substring = command.split(":|:")
            if substring in message:
                message = message.replace(substring, "", 1) # deleting the first occurrence only
                message = message + substring[::-1]
                print(message)
            else:
                print('error')

        elif command.startswith("ChangeAll"):
            current_command, substring, replacement = command.split(":|:")
            message = message.replace(substring, replacement)
            print(message)


data = input()
decrypting_message(data)
