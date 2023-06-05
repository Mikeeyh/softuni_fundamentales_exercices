number = int(input())

number_str = str(number)
digits = list(number_str)
digits.sort(reverse=True)
largest_number = int(''.join(digits))

print(f"The largest number that can be formed is: {largest_number}")
