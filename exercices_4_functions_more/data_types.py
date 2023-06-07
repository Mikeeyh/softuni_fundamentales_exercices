def data_type(element):
    if element == 'int':
        result = int(command) * 2
    elif element == 'real':
        calculation = float(command) * 1.5
        result = f"{calculation:.2f}"
    else:
        result = f"${command}$"

    return result


type_of_element = input()
command = input()
print(data_type(type_of_element))

