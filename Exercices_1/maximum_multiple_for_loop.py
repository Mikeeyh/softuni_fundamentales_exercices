divisor = int(input())
boundary = int(input())
number = 0

for number in range(boundary, divisor - 1, -1):
    if number == 0:   #it is not necessary to add this line because we're actually searching from the highest to lowest.
        continue
    if number % divisor == 0:
        break

print(number)
