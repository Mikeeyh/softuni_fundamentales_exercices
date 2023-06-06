numbers = list(map(int, input().split()))
string = input()
message = ''
string_length = len(string)

for element in numbers:
    digit_sum = sum(int(digit) for digit in str(element))
    index = digit_sum % string_length
    char = string[index]
    message += char
    string = string[:index] + string[index + 1:]
print(message)
