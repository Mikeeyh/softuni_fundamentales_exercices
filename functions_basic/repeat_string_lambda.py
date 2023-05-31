string = input()
counter = int(input())

repeat_string = lambda a, b: a * b
result = repeat_string(string, counter)
print(result)

# OR

string = input()
counter = int(input())
repeat_string = " "


def repeated_string(string_given, counter_given):
    for i in range(counter):
        repeat_string = string * counter
        return repeat_string


result = repeated_string(string, counter)
print(result)
