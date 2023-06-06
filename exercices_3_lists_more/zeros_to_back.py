string = input().split(', ')
list_of_string = []
list_of_zeros = []
list_of_non_zeros = []

for element in string:
    list_of_string.append(int(element))

for digit in list_of_string:
    if digit == 0:
        list_of_zeros.append(int(digit))
    else:
        list_of_non_zeros.append(int(digit))

result = list_of_non_zeros + list_of_zeros
print(list_of_zeros)
print(list_of_non_zeros)
print(result)

# OR ---------------------------------------------------------------------

string = map(int, input().split(', '))
list_of_zeros = []
list_of_non_zeros = []

for digit in string:
    if digit == 0:
        list_of_zeros.append(int(digit))
    else:
        list_of_non_zeros.append(int(digit))

result = list_of_non_zeros + list_of_zeros
print(list_of_zeros)
print(list_of_non_zeros)
print(result)

