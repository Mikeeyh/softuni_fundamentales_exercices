number_of_lines = int(input())
my_list = []
my_filtered_list = []

for line in range(number_of_lines):
    current_number = int(input())
    my_list.append(current_number)
    my_filtered_list.append(current_number)

    if current_number % 2 != 0:
        my_filtered_list.remove(current_number)

print(my_list)
print(my_filtered_list)


