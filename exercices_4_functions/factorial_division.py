def calculate_factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())
first_number_factorial = calculate_factorial(first_number)
second_number_factorial = calculate_factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")

# OR ---------------------------------------------------------------------------------


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

# OR ---------------------------------------------------------------------------------


def factorial_division(num1, num2):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    result1 = factorial(num_1)
    result2 = factorial(num_2)
    division = result1 / result2
    formatted_division = "{:.2f}".format(division)

    print(f"The factorial of {num1} is: {result1}")
    print(f"The factorial of {num2} is: {result2}")
    print(f"The division result is: {formatted_division}")


num_1 = int(input())
num_2 = int(input())
factorial_division(num_1, num_2)

