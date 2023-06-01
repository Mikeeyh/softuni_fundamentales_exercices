first_number, second_number, third_number = int(input()), int(input()), int(input())


def sum_numbers(first, second):
    return first_number + second_number


sum_of_two = sum_numbers(first_number, second_number)


def subtract(sum, third):
    return sum_of_two - third_number


result = subtract(sum_of_two, third_number)
print(result)

