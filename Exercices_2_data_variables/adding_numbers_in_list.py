numbers = []
n = int(input("Choose how many numbers do you want to add in your list: "))
for incoming_numbers in range(n):
    current_number = int(input())
    numbers.append(current_number)
print(numbers)
