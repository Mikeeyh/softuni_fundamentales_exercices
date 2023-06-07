numbers = list(map(int, input().split()))
command = input()
first_list = []
second_list = []

while True:
    if command == 'end':
        break
    command = command.split()
    action = command[0]
    number = int(command[1])

    if action == "exchange":
        if number < 0 or number >= len(numbers):
            print("Invalid index")
        first_list = numbers[:number + 1]
        second_list = numbers[number + 1:]
        print(second_list + first_list)

    command = input()
