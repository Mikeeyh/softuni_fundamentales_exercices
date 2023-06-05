def recursive(number):
    if number == 1:
        return 1
    return number * recursive(number - 1)


given_number = int(input('Please choose a number: '))
print(recursive(given_number))

# OR----------------------------------------------------------------------------


def recursive(number):
    if number == 1:
        return 1
    return number * recursive(number - 1)


first_number = int(input('Please choose a number: '))
second_number = int(input('Please choose a number: '))
result = recursive(first_number) / recursive(second_number)
print(recursive(first_number))
print(recursive(second_number))
print(f"{result:.2f}")


