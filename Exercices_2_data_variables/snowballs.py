number_of_balls = int(input())
max_value = 0
max_weight = 0
max_time_needed = 0
max_quality = 0

for snowball in range(number_of_balls):
    current_weight = int(input())
    current_time_needed = int(input())
    current_quality = int(input())

    current_value = (current_weight / current_time_needed) ** current_quality

    if current_value > max_value:
        max_value = current_value
        max_weight = current_weight
        max_time_needed = current_time_needed
        max_quality = current_quality


print(f"{max_weight} : {max_time_needed} = {int(max_value)} ({max_quality})")
