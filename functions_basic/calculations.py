input_operator = input()
first_number = int(input())
second_number = int(input())


def solve(operator, first_num, second_num):
    result = ''
    if operator == "multiply":
        result = first_num * second_num
    elif operator == "divide":
        result = first_num / second_num
    elif operator == "add":
        result = first_num + second_num
    elif operator == "subtract":
        result = first_num - second_num
    return "{:.0f}".format(result)


print(solve(input_operator, first_number, second_number))
