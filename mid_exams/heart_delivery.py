numbers = list(map(int, input().split('@')))
command = input()
position = 0

while command != 'Love!':

    command = command.split()
    action = command[0]
    index = int(command[1])
    if action == 'Jump':
        position = (position + index) % len(numbers)

    if numbers[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        numbers[position] -= 2
        if numbers[position] == 0:
            print(f"Place {position} has Valentine's day.")

    command = input()

houses_not_celebrated = sum(hearts > 0 for hearts in numbers)

print(f"Cupid's last position was {position}.")
if houses_not_celebrated == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {houses_not_celebrated} places.")
