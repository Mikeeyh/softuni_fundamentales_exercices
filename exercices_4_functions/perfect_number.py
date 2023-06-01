given_number = int(input())


def is_perfect_number(num):
    divisors_sum = 0

    for i in range(1, given_number):
        if given_number % i == 0:
            divisors_sum += i

    if divisors_sum == given_number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


is_perfect_number(given_number)
