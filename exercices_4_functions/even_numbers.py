string_of_numbers = input().split()


def is_even(number):
    list_of_numbers = []
    for num in string_of_numbers:
        current_number = int(num)
        if current_number % 2 == 0:
            list_of_numbers.append(current_number)
    return list_of_numbers


result = is_even(string_of_numbers)
print(result)


# OR USING FILTER:

string_of_numbers = input().split()


def str_to_int_list_converter(number):
    list_of_numbers = []
    for num in string_of_numbers:
        current_number = int(num)
        list_of_numbers.append(current_number)
    return list_of_numbers


def is_even(number):
    return number % 2 == 0


even_numbers_list = list(filter(is_even, str_to_int_list_converter(string_of_numbers)))
print(even_numbers_list)

