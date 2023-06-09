message = input()
words = message.split()
reversed_words = []
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
    new_word = left_part + right_part
    reversed_words.append(new_word)
    digit = ''
    letter = ''
    index = 0

print(reversed_words)






