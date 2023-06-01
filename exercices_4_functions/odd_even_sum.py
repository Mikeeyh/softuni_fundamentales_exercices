string_of_numbers = input()


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


print(odd_even_filter(string_of_numbers))

