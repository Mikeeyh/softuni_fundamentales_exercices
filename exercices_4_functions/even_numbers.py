def is_even(number):
    list_of_numbers = []
    for num in string_of_numbers:
        current_number = int(num)
        if current_number % 2 == 0:
            list_of_numbers.append(current_number)
    return list_of_numbers


string_of_numbers = input().split()
result = is_even(string_of_numbers)
print(result)


# OR USING FILTER: ------------------------------------------------------------------------------


def str_to_int_list_converter(number):
    list_of_numbers = []
    for num in string_of_numbers:
        list_of_numbers.append(int(num))
    return list_of_numbers


def is_even(number):
    return number % 2 == 0


string_of_numbers = input().split()
even_numbers_list = list(filter(is_even, str_to_int_list_converter(string_of_numbers)))
print(even_numbers_list)


# OR USING FILTER: -------------------------------------------------------------------------------

numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number)) #or number_as_digits = [int(number) for number in numbers_as_string

is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)

# OR IN ONE LINE ----------------------------------------------------------------------------------------

print([int(number) for number in input().split() if int(number) % 2 == 0])
