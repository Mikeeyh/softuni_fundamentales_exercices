string = input()

result = ""
skip_count = 0

numbers = [int(element) for element in string if element.isdigit()]
non_numbers = [element for element in string if not element.isdigit()]

take_list = [numbers[index] for index in range(len(numbers)) if index % 2 == 0]
skip_list = [numbers[index] for index in range(len(numbers)) if index % 2 != 0]

for take, skip in zip(take_list, skip_list):
    result += "".join(non_numbers[:take])
    non_numbers = non_numbers[take + skip:]

print(result)

# OR -----------------------------------------------------------------------------

import re

def extract_hidden_message(string):
    numbers = [int(digit) for digit in string if digit.isdigit()]
    non_numbers = re.findall('[^0-9]', string)

    take_list = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
    skip_list = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

    result = ''
    skip_count = 0

    for take, skip in zip(take_list, skip_list):
        result += ''.join(non_numbers[:take])
        non_numbers = non_numbers[take + skip:]
        skip_count += skip

    result += ''.join(non_numbers[skip_count:])

    return result


input_string = input()
hidden_message = extract_hidden_message(input_string)
print(hidden_message)
