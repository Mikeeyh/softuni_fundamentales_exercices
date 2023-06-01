string_of_numbers = input().split()


def string_to_list(string):
    list_of_numbers = []
    for number in string_of_numbers:
        current_number = int(number)
        list_of_numbers.append(int(current_number))
        list_of_numbers.sort(reverse=False)
    return list_of_numbers


result = string_to_list(string_of_numbers)
print(result)

