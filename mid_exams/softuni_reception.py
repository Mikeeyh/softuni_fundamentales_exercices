employee1_efficiency = int(input())
employee2_efficiency = int(input())
employee3_efficiency = int(input())
students_count = int(input())
breaks = 0

total_efficiency = employee1_efficiency + employee2_efficiency + employee3_efficiency
total_time = students_count // total_efficiency

if students_count % total_efficiency != 0:
    total_time += 1

for break_count in range(total_time):
    breaks += 1
    if breaks % 4 == 0:
        breaks = 0
        total_time += 1

print(f"Time needed: {total_time}h.")
