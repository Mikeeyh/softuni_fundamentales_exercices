def fill_shells(electrons):
    shells = []
    shell_number = 1

    while electrons > 0:
        adding_electrons = 2 * shell_number**2

        if electrons >= adding_electrons:
            shells.append(adding_electrons)
            electrons -= adding_electrons
        else:
            shells.append(electrons)
            electrons = 0
        shell_number += 1
    return shells


num_electrons = int(input())
filled_shells = fill_shells(num_electrons)
print(filled_shells)

# OR ----------------------------------------

number_of_electrons = int(input())
list_of_electrons = []
current_index = 1

while number_of_electrons > 0:

    electrons = 2 * current_index ** 2

    if number_of_electrons >= electrons:
        list_of_electrons.append(electrons)
        number_of_electrons -= electrons
    else:
        list_of_electrons.append(number_of_electrons)
        number_of_electrons = 0

    current_index += 1

print(list_of_electrons)
