from math import ceil, floor

students = int(input())
lectures = int(input())
additional_bonus = int(input())
bonus_list = []

for student in range(students):
    attendance = int(input())
    total_bonus = attendance / lectures * (5 + additional_bonus)
    bonus_list.append(total_bonus)

biggest_bonus = ceil(max(bonus_list))
attendance_winner = floor((biggest_bonus / (5 + additional_bonus)) * lectures)

print(f"Max Bonus: {biggest_bonus}.")
print(f"The student has attended {attendance_winner} lectures.")
