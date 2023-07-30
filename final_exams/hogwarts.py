string = input()

while True:
    command = input().split()
    action = command[0]

    if action == 'Abracadabra':
        break

    elif action == 'Abjuration':
        string = string.upper()
        print(string)

    elif action == 'Necromancy':
        string = string.lower()
        print(string)

    elif action == 'Illusion':
        index = int(command[1])
        letter = command[2]

        if 0 < index < len(string):
            string = string[:index] + letter + string[index + 1:]
            print("Done!")
        else:
            print("The spell was too weak.")

    elif action == 'Divination':
        first_substring = command[1]
        second_substring = command[2]
        if first_substring in string:
            string = string.replace(first_substring, second_substring)
            print(string)

    elif action == 'Alteration':
        substring = command[1]
        if substring in string:
            string = string.replace(substring, "")
            print(string)

    else:
        print("The spell did not work!")
