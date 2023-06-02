def smallest_number(first, second, third):
    return min(first_number, second_number, third_number)


first_number, second_number, third_number = int(input()), int(input()), int(input())

min_number = smallest_number(first_number, second_number, third_number)
print(min_number)

# OR


def smallest_number(some_numbers):
    min_element = min(some_numbers)
    return min_element


first_number, second_number, third_number = int(input()), int(input()), int(input())
numbers_list = [first_number, second_number, third_number]
print(smallest_number(numbers_list))

