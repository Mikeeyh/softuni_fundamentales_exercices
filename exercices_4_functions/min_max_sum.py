string_of_numbers = input().split()


def string_to_list(numbers):
    list_of_numbers = []
    for number in string_of_numbers:
        current_number = int(number)
        list_of_numbers.append(current_number)
        list_of_numbers.sort(reverse=False)
    return list_of_numbers


# result = string_to_list(string_of_numbers)
# print(result)


def min_num(nums):
    print(f"The minimum number is {min(string_to_list(string_of_numbers))}")


min_num(string_to_list)


def max_num(nums):
    print(f"The maximum number is {max(string_to_list(string_of_numbers))}")


max_num(string_to_list)


def sum_num(nums):
    print(f"The sum number is: {sum(string_to_list(string_of_numbers))}")


sum_num(string_to_list)
