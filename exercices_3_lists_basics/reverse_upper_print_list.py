my_list = ["hello", "world", "python", "magic"]
index = 0

while index < len(my_list):
    current_word = my_list[index]
    modified_word = ''

    for char in reversed(current_word):
        modified_word += char.upper()

    print(modified_word)
    index += 1
