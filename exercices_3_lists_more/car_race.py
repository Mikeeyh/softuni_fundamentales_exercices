sequence_of_numbers = list(map(int, input().split()))
left_side = []
right_side = []
counter_left = 0
counter_right = 0
index_middle = 0
total_time_left = 0
total_time_right = 0

for character_index in range(len(sequence_of_numbers)):

    index_middle = len(sequence_of_numbers) // 2
    if character_index == index_middle:
        break

    # if counter_left == len(sequence_of_numbers) // 2:
    #     if counter_right == len(sequence_of_numbers) // 2:
    #         if index_middle == 1:
    #             break

    left_side = sequence_of_numbers[:character_index + 1]
    right_side = sequence_of_numbers[character_index + 2:]
    counter_left += 1
    counter_right += 1

    # index_middle = len(sequence_of_numbers) - (counter_right + counter_left)

mid_position = sequence_of_numbers[counter_left]

for i in left_side:
    if i == 0:
        total_time_left *= 0.8
    total_time_left += i

for i in right_side:
    if i == 0:
        total_time_right *= 0.8
    total_time_right += i

result = min(total_time_left, total_time_right)
if min(total_time_left, total_time_right) == total_time_left:
    winner = 'left'
else:
    winner = 'right'

print(f"The winner is {winner} with total time: {result:.1f}")
