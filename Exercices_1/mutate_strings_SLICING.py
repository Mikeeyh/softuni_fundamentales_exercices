"""
name = "PetarIvanov"
print(name[1:3]) # we take index 1,2 without 3 ||| et
print(name[1:5:2]) # we take index 1,3 without 5 (with step 2) ||| ea
print(name[1:]) # we take all index despite 0 (from index 1 to final index) ||| etarIvanov
print(name[:5]) # we take all index from 5 to 0 |||  Petar
print(name[::-1]) # we print the name unversed ||| vonavIrateP (it is like a for loop from the end to the beginning)
"""

first_string = input()
second_string = input()

last_printed_string = first_string

for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    new_string = left_part + right_part

    if new_string == last_printed_string:
        continue
    print(new_string)
    last_printed_string = new_string
