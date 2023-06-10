message = input()
words = message.split()
digit = ''
letter = ''
index = 0

for word in words:
    for character in word:
        if character.isdigit():
            digit += character
            letter = chr(int(digit))
            index += 1

    left_part = letter
    right_part = word[index:]
    new_word = list(left_part + right_part)

    if index == 2:
        new_word[index - 1], new_word[-1] = new_word[-1], new_word[index - 1]
    elif index == 3:
        new_word[index - 2], new_word[-1] = new_word[-1], new_word[index - 2]

    print(''.join(new_word), end=' ')

    digit = ''
    letter = ''
    index = 0


