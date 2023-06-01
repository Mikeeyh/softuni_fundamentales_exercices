string_of_numbers = input().split(", ")


def palindrome_filter(numbers):
    for number in string_of_numbers:
        number_converted_as_string = str(number)

        if number_converted_as_string == number_converted_as_string[::-1]:
            print(f"True")
        else:
            print(f"False")


palindrome_filter(string_of_numbers)
