def recursive(number):
    if number == 1:
        return 1
    return number * recursive(number - 1)


given_number = int(input('Please choose a number: '))
print(recursive(given_number))
