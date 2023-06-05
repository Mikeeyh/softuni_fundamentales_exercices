key = int(input())
number_of_letters = int(input())
decrypted_list = []

for character in range(number_of_letters):
    current_character = input()
    current_character = ord(current_character) + key
    decrypted_list.append(chr(current_character))
print(''.join(decrypted_list))



