employee1_efficiency = int(input())
employee2_efficiency = int(input())
employee3_efficiency = int(input())
students_count = int(input())

total_efficiency = employee1_efficiency + employee2_efficiency + employee3_efficiency
total_time = students_count // total_efficiency

if students_count % total_efficiency != 0:
    total_time += 1

breaks = total_time // 4
total_time += breaks

print(f"Time needed: {total_time}h.")
