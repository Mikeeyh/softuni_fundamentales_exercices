array_numbers = list(map(int, input().split()))
command = input()

while command != "end":
    command = command.split()
    action = command[0]

    if action == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        array_numbers[index_1], array_numbers[index_2] = array_numbers[index_2], array_numbers[index_1]

    elif action == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        array_numbers[index_1] *= array_numbers[index_2]

    elif action == "decrease":
        array_numbers = [num - 1 for num in array_numbers]

    command = input()

print(*array_numbers, sep=", ")
# output = ", ".join([str(num) for num in array])
# print(output)
