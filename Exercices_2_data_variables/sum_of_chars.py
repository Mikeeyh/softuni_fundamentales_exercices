n = int(input())
sum = 0

for i in range(n):
    current_character = input()
    number = ord(current_character)
    sum += number

print(f"The sum equals: {sum}")