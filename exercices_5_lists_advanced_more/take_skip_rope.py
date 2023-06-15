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
