text = input()
final_text = ''
last_character = ''

for current_char in text:
    if current_char != last_character:
        final_text += current_char
        last_character = current_char

print(final_text)