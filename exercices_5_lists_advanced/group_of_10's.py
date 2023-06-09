numbers = [int(num) for num in input().split(', ')]
current_group_of_numbers = 10

while numbers:       # numbers > 0

    filtered_numbers_for_current_group = [number for number in numbers if number <= current_group_of_numbers]

    print(f"Group of {current_group_of_numbers}'s: {filtered_numbers_for_current_group}")
    current_group_of_numbers += 10

    numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]
