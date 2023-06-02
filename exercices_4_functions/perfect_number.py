def is_perfect_number(given_number):
    divisors_sum = 0

    for divisor in range(1, given_number):
        if given_number % divisor == 0:
            divisors_sum += divisor

    if given_number == divisors_sum:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect_number(number))

# OR ------------------------------------------------------------------------------------------------


def is_perfect_number(given_number):      #as per convention:           def is_perfect_number(num: int) -> str:
    divisors_sum = 0

    for divisor in range(1, given_number):
        if given_number % divisor == 0:
            divisors_sum += divisor

    if given_number == divisors_sum:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
is_perfect_number(number)

