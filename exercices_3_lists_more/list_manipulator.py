numbers = list(map(int, input().split()))
command = input()
first_list = []
second_list = []

while True:
    if command == 'end':
        break
    command = command.split()
    action = command[0]
    second_action = command[1]

    if action == "exchange":
        second_action = int(command[1])
        number = second_action
        if number < 0 or number >= len(numbers):
            print("Invalid index")
        else:
            first_list = numbers[:number + 1]
            second_list = numbers[number + 1:]
            print(second_list + first_list)

    if action == "max":
        if second_action == "even":
            filtered_list = [num for num in numbers if num % 2 == 0]
            if not filtered_list:
                print('No matches')
            else:
                max_num = max(filtered_list)
                max_index = len(numbers) - 1 - numbers[::-1].index(max_num)
                print(max_index)
        elif second_action == "odd":
            filtered_list = [num for num in numbers if num % 2 != 0]
            if not filtered_list:
                print('No matches')
            else:
                max_num = max(filtered_list)
                max_index = len(numbers) - 1 - numbers[::-1].index(max_num)
                print(max_index)

    if action == "min":
        if second_action == "even":
            filtered_list = [num for num in numbers if num % 2 == 0]
            if not filtered_list:
                print('No matches')
            else:
                min_num = min(filtered_list)
                min_index = len(numbers) - 1 - numbers[::-1].index(min_num)
                print(min_index)
        elif second_action == "odd":
            filtered_list = [num for num in numbers if num % 2 != 0]
            if not filtered_list:
                print('No matches')
            else:
                min_num = min(filtered_list)
                min_index = len(numbers) - 1 - numbers[::-1].index(min_num)
                print(min_index)

    command = input()
