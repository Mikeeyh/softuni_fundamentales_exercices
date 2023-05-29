number_of_lines = int(input())
positive_numbers = []
negative_numbers = []
count_of_positive_numbers = 0
sum_of_negative_numbers = 0

for line in range(number_of_lines):
    current_number = int(input())

    if current_number >= 0:
        positive_numbers.append(current_number)
        count_of_positive_numbers += 1
    else:
        negative_numbers.append(current_number)
        sum_of_negative_numbers += current_number

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {count_of_positive_numbers}")
print(f"Sum of negatives: {sum_of_negative_numbers}")
