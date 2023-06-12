numbers = input().split()
count_of_numbers = 0
total_number = 0
list_of_numbers = []
filtered_numbers = []
flag = False

for num in range(len(numbers)):
    list_of_numbers.append(int(numbers[num]))
    list_of_numbers.sort(reverse=True)
    count_of_numbers += 1
    total_number += int(numbers[num])

average_number = total_number / count_of_numbers
counter = 0

for current_number in list_of_numbers:
    if current_number > average_number:
        if counter < 5:
            filtered_numbers.append(current_number)
            counter += 1

if counter == 0:
    flag = True

if flag:
    print('No')
else:
    print(*filtered_numbers, end=' ')

