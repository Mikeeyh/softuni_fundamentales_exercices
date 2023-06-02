def odd_even_numbers(some_number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)

    return sum_of_odd_digits, sum_of_even_digits


number = input()
odd_digits, even_digits = odd_even_numbers(number)
print(f'Odd sum = {odd_digits}, Even sum = {even_digits}')


# OR --------------


def string_to_list(string):
    list_of_numbers = []
    for i in range(len(string_of_numbers)):
        current_string = string_of_numbers[i]
        list_of_numbers.append(int(current_string))
    return list_of_numbers


def odd_even_filter(numbers):
    sum_even = 0
    sum_odd = 0
    for number in string_to_list(string_of_numbers):
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number
    return f'Odd sum = {sum_odd}, Even sum = {sum_even}'


string_of_numbers = input()
print(odd_even_filter(string_of_numbers))



