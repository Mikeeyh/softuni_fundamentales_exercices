num_1 = int(input())
num_2 = int(input())


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


factorial_division(num_1, num_2)

