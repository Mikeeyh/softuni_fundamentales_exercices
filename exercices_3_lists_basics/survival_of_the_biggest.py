list_of_integer_string = input().split()
numbers_to_be_removed = int(input())
my_list = []

for number in list_of_integer_string:
    my_list.append(int(number))

for index in range(numbers_to_be_removed):
    my_list.remove(min(my_list))

print(*my_list, sep=", ")