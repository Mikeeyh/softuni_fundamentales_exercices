def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


first_number, second_number, third_number = int(input()), int(input()), int(input())
sum_of_two = sum_numbers(first_number, second_number)
result = subtract(sum_of_two, third_number)
print(result)

# OR -------------------------------------------------------------------------


def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


def add_subtract(number_one, number_two, number_three):
    sum_of_first_and_second_numbers = sum_numbers(number_one, number_two)
    result = subtract(sum_of_first_and_second_numbers, number_three)
    return result #or print(result)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_subtract(first_number, second_number, third_number)) #or add_subtract(first_number, third_number)

