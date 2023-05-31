# number_string = input().split()
#
#
# def round_numbers(number_strings):
#     rounded_numbers = [int(round(float(num))) for num in number_string]
#     return rounded_numbers
#
#
# rounded_list = round_numbers(number_string)
# print(rounded_list)

number_string = input().split()
rounded_numbers = []


def round_numbers(number_strings):
    for num in number_string:
        element = int(round(float(num)))
        rounded_numbers.append(element)
    return rounded_numbers


rounded_list = round_numbers(number_string)
print(rounded_list)
