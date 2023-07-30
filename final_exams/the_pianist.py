n = int(input())
pieces_dict = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces_dict[piece] = [composer, key]

while True:
    command = input()
    command_data = command.split('|')
    action = command_data[0]

    if action == 'Stop':
        for piece_current, data in pieces_dict.items():
            composer_current = data[0]
            key_current = data[1]
            print(f"{piece_current} -> Composer: {composer_current}, Key: {key_current}")
        break

    if action == 'Add':
        piece = command_data[1]
        composer = command_data[2]
        key = command_data[3]

        if piece in pieces_dict:
            print(f"{piece} is already in the collection!")
        else:
            pieces_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == 'Remove':
        piece = command_data[1]
        if piece in pieces_dict:
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == 'ChangeKey':
        piece = command_data[1]
        new_key = command_data[2]
        if piece in pieces_dict:
            pieces_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

# OR ----------------------------------------------------


def create_composer_data(number_of_pieces):
    composer_dictionary = {}

    for _ in range(number_of_pieces):
        piece, composer, key = input().split("|")
        composer_dictionary[piece] = [composer, key]

    return composer_dictionary


def modifying_data_function(composer_dictionary):

    while True:
        command, *params = input().split("|")

        if command == 'Stop':
            return composer_dictionary

        elif command == 'Add':
            piece, composer, key = params[0], params[1], params[2]

            if piece in composer_dictionary:
                print(f"{piece} is already in the collection!")
            else:
                composer_dictionary[piece] = [composer, key]
                print(f"{piece} by {composer} in {key} added to the collection!")

        elif command == 'Remove':
            piece = params[0]

            if piece in composer_dictionary:
                del composer_dictionary[piece]
                print(f"Successfully removed {piece}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")

        elif command == 'ChangeKey':
            piece, new_key = params[0], params[1]

            if piece in composer_dictionary:
                composer_dictionary[piece][1] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")


def base_function(number_of_pieces):
    composer_dictionary = create_composer_data(number_of_pieces)
    modifying_dictionary = modifying_data_function(composer_dictionary)

    for piece, data in modifying_dictionary.items():
        composer = data[0]
        key = data[1]
        print(f"{piece} -> Composer: {composer}, Key: {key}")


n = int(input())
base_function(n)
