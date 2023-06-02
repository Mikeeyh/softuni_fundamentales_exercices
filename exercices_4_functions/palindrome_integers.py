def check_palindrome(some_number):
    if some_number == some_number[::-1]:
        return True
    return False


numbers = input().split(", ")
for number in numbers:
    print(check_palindrome(number))


# OR -------------------------------------------

def palindrome_filter(num):
    for num in string_of_numbers:
        number_converted_as_string = str(num)

        if number_converted_as_string == number_converted_as_string[::-1]:
            print(f"True")
        else:
            print(f"False")


string_of_numbers = input().split(", ")
palindrome_filter(string_of_numbers)
